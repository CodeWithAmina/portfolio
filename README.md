# Portfolio (Flask)

This is a simple personal portfolio and online resume built with Flask. It includes:

- About / Education & Skills
- Projects / Achievements
- Contact form (sends email via SMTP or prints to console for local testing)
- Light / Dark theme and alert UI

Quick start (Windows PowerShell)

1. Create a virtualenv and install dependencies:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

2. (Optional) Configure SMTP env vars to enable live email sending. Example (Gmail app password):

```powershell
$env:MAIL_SERVER='smtp.gmail.com'
$env:MAIL_PORT='587'
$env:MAIL_USERNAME='your.email@gmail.com'
$env:MAIL_PASSWORD='your-app-password'
$env:FROM_EMAIL='your.email@gmail.com'
$env:TO_EMAIL='your.receiving.email@example.com'
$env:SECRET_KEY='replace-with-a-secure-secret'
```

If SMTP vars are not set, submitted messages will be printed to the server console (safe for local testing).

3. Run the app:

```powershell
python .\app.py

# then open http://localhost:5000
```

Deployment notes

- Render or Railway are simple hosting options for small Flask apps. Create a service, connect your GitHub repo, set the env vars listed above in the platform UI, and add `gunicorn` to `requirements.txt` if required by your host.
- For production don't use the built-in Flask server; use a WSGI server such as `gunicorn`.

LinkedIn networking task (assignment guidance)

1. Connect with at least 3 HR professionals or recruiters. Use a short, polite connection message like:

"Hi [Name], I'm building my online portfolio and preparing to apply for junior web developer roles. I'd appreciate any quick advice on the technical and soft skills recruiters look for. Here's my portfolio: <link>. Thanks!"

2. Ask two things:
- What technical and soft skills they expect from fresh web developers
- If they can share resume feedback (you may include your portfolio link)

3. After conversations, write a 150–200 word summary of what you learned and attach screenshots of the chats as proof.

Summary template (150–200 words):

"I reached out to three HR professionals and learned that employers prioritize practical experience with version control (Git), familiarity with REST APIs, and a basic understanding of databases. Recruiters emphasized soft skills such as communication, teamwork, and a willingness to learn. Several suggested adding concise case-studies in my portfolio that show the problem, approach, and outcome. One recruiter recommended highlighting testing and deployment experience (CI/CD), while another valued clear README files and live links to demos. Resume feedback focused on clear role-based bullet points, quantifiable outcomes, and removing unrelated coursework. Overall, the responses reinforced the importance of demonstrable projects, concise storytelling in the resume, and an active LinkedIn profile. I'll update my portfolio accordingly and follow up with the contacts to thank them."

Screenshots checklist:
- Capture the connection acceptance and the short advice messages
- Include timestamps and the recruiter's name/role
- Save images as PNG or JPG and attach them to your Moodle submission
