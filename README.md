# GitCheck 2.0 🔐  
A Lightweight GitHub Repository Vulnerability Scanner

GitCheck 2.0 is a security-focused web application that scans GitHub repositories for potential vulnerabilities using **Semgrep** and presents the results through a simple **Django-based API and UI**.  
The project is designed to demonstrate **secure code analysis**, **backend engineering**, and **tool integration**, making it suitable for cybersecurity and backend roles.

---

## 🚀 Features

- 🔍 Scan public GitHub repositories for vulnerabilities
- 🛡 Uses **Semgrep** for static code analysis
- 🌐 REST API built with **Django**
- 🖥 Minimal web UI for submitting repository URLs
- 🗂 Stores scan history in a database
- 💻 Works on **Windows (tested)**

---

## 🛠 Tech Stack

- **Backend**: Python, Django  
- **Security Scanner**: Semgrep (CLI)  
- **Database**: SQLite (default)  
- **Frontend**: HTML, CSS, JavaScript  
- **Version Control**: Git & GitHub  

---

## 📁 Project Structure
GitCheck-2.0/ │ ├── api/ │   ├── migrations/ │   ├── static/api/ │   ├── templates/api/ │   ├── models.py │   ├── views.py │   ├── urls.py │   └── admin.py │ ├── core/ │   ├── settings.py │   ├── urls.py │   ├── asgi.py │   └── wsgi.py │ ├── manage.py ├── requirements.txt ├── README.md └── db.sqlite3
Copy code

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository
```bash
git clone https://github.com/PERRY276/GitCheck-2.0.git
cd GitCheck-2.0
2️⃣ Create & activate virtual environment (Windows)
Copy code
Bash
python -m venv venv
venv\Scripts\activate
3️⃣ Install dependencies
Copy code
Bash
pip install -r requirements.txt
4️⃣ Install Semgrep
Copy code
Bash
pip install semgrep
Verify installation:
Copy code
Bash
semgrep --version
5️⃣ Run database migrations
Copy code
Bash
python manage.py makemigrations
python manage.py migrate
6️⃣ Start the development server
Copy code
Bash
python manage.py runserver
Server will run at:
Copy code

http://127.0.0.1:8000/
🔌 API Usage
▶ Scan a GitHub Repository
Endpoint
Copy code

POST /api/scan/
Request Body (JSON)
Copy code
Json
{
  "repo_url": "https://github.com/pallets/flask"
}
Response
Copy code
Json
{
  "status": "ok",
  "scan_id": 1
}
▶ View Scan History
Copy code

GET /api/history/
🖥 Web UI
Open browser at:
Copy code

http://127.0.0.1:8000/api/
Paste a public GitHub repository URL
Submit to trigger a scan
⚠️ Notes & Limitations
Only public GitHub repositories are supported
Designed for learning & demonstration, not production use
Semgrep rules depend on default configuration
Tested on Windows OS
🎯 Learning Outcomes
This project demonstrates:
Static Application Security Testing (SAST)
Django REST-style API design
Integrating CLI security tools into web backends
Handling real-world GitHub repositories
Secure project structuring and deployment basics
📌 Future Improvements
Add authentication
Support private repositories
Improve UI/UX
Add severity-based filtering
Integrate local AI (Ollama) for fix recommendations
👤 Author
Pranjal Padhiyar
Computer Science / IT Student
Interested in Backend Development & Cybersecurity
📜 License
This project is for educational purposes.
Copy code

---

## ✅ What to do now (important)

After replacing your `README.md` with this:

```bash
git add README.md
git rebase --continue
git push -u origin main