async function scanRepo() {
    const repoUrl = document.getElementById("repoInput").value;
    const output = document.getElementById("output");

    output.textContent = "Scanning...";

    try {
        const response = await fetch("/api/scan/", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ repo_url: repoUrl })
        });

        const data = await response.json();
        output.textContent = JSON.stringify(data, null, 2);

    } catch (err) {
        output.textContent = "Error: " + err;
    }
}
