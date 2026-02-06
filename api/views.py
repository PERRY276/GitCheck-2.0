import json
import tempfile
import subprocess
import shutil
import os
import requests

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render

from .models import Scan


@csrf_exempt
def scan_repo(request):
    if request.method != "POST":
        return JsonResponse({"error": "POST only"}, status=405)

    try:
        data = json.loads(request.body.decode("utf-8"))
        repo_url = data.get("repo_url")
        if not repo_url:
            return JsonResponse({"error": "repo_url required"}, status=400)
    except Exception:
        return JsonResponse({"error": "Invalid JSON"}, status=400)

    scan = Scan.objects.create(repo_url=repo_url, status="RUNNING")

    temp_dir = tempfile.mkdtemp()

    try:
        # clone repo
        subprocess.run(
            ["git", "clone", repo_url, temp_dir],
            check=True,
            capture_output=True,
            text=True
        )

        # force UTF-8 everywhere
        env = os.environ.copy()
        env["PYTHONUTF8"] = "1"
        env["PYTHONIOENCODING"] = "utf-8"
        env["SEMGRP_DISABLE_VERSION_CHECK"] = "1"

        semgrep = subprocess.run(
            [
                "semgrep",
                "--config=p/security-audit",
                "--json",
                temp_dir
            ],
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            env=env
        )

        if semgrep.returncode not in (0, 1):
            raise Exception(semgrep.stderr)

        result = json.loads(semgrep.stdout or "{}")
        issues = result.get("results", [])

        enriched_issues = []

        for issue in issues[:5]:  # limit to avoid slow AI calls
            explanation = explain_issue_with_ollama(issue)
            enriched_issues.append({
                "rule_id": issue.get("check_id"),
                "severity": issue.get("extra", {}).get("severity"),
                "message": issue.get("extra", {}).get("message"),
                "file": issue.get("path"),
                "explanation": explanation
            })


        scan.status = "COMPLETED"
        scan.save()

        return JsonResponse({
            "scan_id": scan.id,
            "issues_found": len(issues),
            "issues": enriched_issues
        })


    except Exception as e:
        scan.status = "FAILED"
        scan.save()
        return JsonResponse({"error": str(e)}, status=500)

    finally:
        shutil.rmtree(temp_dir, ignore_errors=True)

def scan_history(request):
    scans = Scan.objects.order_by("-created_at").values()
    return JsonResponse(list(scans), safe=False)

def explain_issue_with_ollama(issue):
    prompt = f"""
You are a security expert.

Explain this vulnerability in simple terms and suggest a fix.

Rule ID: {issue.get('check_id')}
Message: {issue.get('extra', {}).get('message')}
Severity: {issue.get('extra', {}).get('severity')}
Language: {issue.get('language')}

Answer format:
- Explanation
- Why it's dangerous
- How to fix
"""

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama3.2:1b",
            "prompt": prompt,
            "stream": False
        },
        timeout=60
    )

    return response.json().get("response", "").strip()


def index(request):
    return render(request, "api/index.html")


