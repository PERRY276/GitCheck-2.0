from django.db import models

class Scan(models.Model):
    repo_url = models.URLField()
    total_issues = models.IntegerField(default=0)
    high_issues = models.IntegerField(default=0)
    medium_issues = models.IntegerField(default=0)
    low_issues = models.IntegerField(default=0)

    raw_report = models.JSONField(null=True, blank=True)

    status = models.CharField(max_length=20, default="PENDING")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.repo_url
