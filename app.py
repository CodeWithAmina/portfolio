import os
import smtplib
import ssl
from datetime import datetime
from email.message import EmailMessage

from flask import Flask, render_template, request

app = Flask(__name__)

SKILL_CATEGORIES = [
    {"name": "Programming languages", "skills": ["Python", "Java", "C"]},
    {"name": "Frontend development", "skills": ["HTML5", "CSS3", "JavaScript", "React"]},
    {"name": "Backend development", "skills": ["Django", "Flask", "PHP", "REST APIs"]},
    {"name": "Databases", "skills": ["MySQL", "SQLite", "SQL"]},
    {"name": "AI & machine learning", "skills": ["TensorFlow", "Deep Learning", "Machine Learning", "NLP", "Data Preprocessing"]},
    {"name": "Tools & technologies", "skills": ["Git", "GitHub", "Android Studio", "VS Code", "Jupyter Notebook"]},
]

PROJECTS = [
    {
        "name": "CyberShield",
        "category": "Deep learning · Artificial intelligence",
        "description": "A text-classification application exploring how NLP and a Bidirectional LSTM model can identify cyberbullying in social media text.",
        "technologies": ["Python", "TensorFlow", "BiLSTM", "NLP", "Tkinter"],
        "features": [
            "Text preprocessing and cleaning",
            "BiLSTM-based cyberbullying classification",
            "Interactive Tkinter desktop interface",
            "Real-time text prediction",
        ],
        "theme": "coral",
        "art_label": "TEXT SAFETY",
        "symbol": "///",
        "github": None,
        "demo": None,
    },
    {
        "name": "FoodRescue",
        "category": "Android application development",
        "description": "A mobile application connecting food donors and students to help redistribute surplus food and reduce food waste.",
        "technologies": ["Java", "XML", "Android Studio", "SQLite"],
        "features": [
            "Student and organizer registration",
            "Surplus food listings with quantity, location, image, and pickup time",
            "Browse, claim, and manage claim status",
            "Local notifications and SQLite storage",
            "Supports SDG 2: Zero Hunger and SDG 12: Responsible Consumption and Production",
        ],
        "theme": "sage",
        "art_label": "SHARE MORE · WASTE LESS",
        "symbol": "+",
        "github": None,
        "demo": None,
    },
    {
        "name": "Parudeesa Resort",
        "category": "Full stack web development",
        "description": "A resort and event booking management system designed to bring reservations and administrative operations into one web application.",
        "technologies": ["Laravel", "PHP", "MySQL", "JavaScript", "HTML", "CSS", "Google Calendar"],
        "features": [
            "Room reservation and event booking management",
            "Administrative dashboard and reservation management",
            "Google Calendar integration",
            "Chatbot and payment gateway integrations",
        ],
        "theme": "sand",
        "art_label": "STAY · GATHER · CELEBRATE",
        "symbol": "P.",
        "github": None,
        "demo": None,
    },
    {
        "name": "IoT Smart Monitoring",
        "category": "Internet of Things",
        "description": "A sensor-based monitoring solution that collects environmental data and makes it available through MQTT communication and a web dashboard.",
        "technologies": ["Python", "ESP32", "MQTT", "Flask", "DHT22", "PIR", "LDR"],
        "features": [
            "Temperature and humidity monitoring",
            "PIR motion detection and LDR light-intensity monitoring",
            "MQTT sensor data communication",
            "Web-based sensor monitoring dashboard",
        ],
        "theme": "blue",
        "art_label": "SENSOR NETWORK",
        "symbol": "⌁",
        "github": None,
        "demo": None,
    },
]


@app.context_processor
def inject_site_data():
    return {
        "current_year": datetime.now().year,
        "projects": PROJECTS,
        "skill_categories": SKILL_CATEGORIES,
    }


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/contact', methods=['POST'])
def submit_contact():
    name = request.form.get('name', '').strip()
    sender_email = request.form.get('email', '').strip()
    message = request.form.get('message', '').strip()
    form_message = None
    form_error = False

    if not name or not sender_email or not message:
        form_message = 'Please complete all fields before sending your message.'
        form_error = True
    elif (
        len(name) > 120
        or len(sender_email) > 254
        or len(message) > 5000
        or '\n' in name
        or '\r' in name
        or '\n' in sender_email
        or '\r' in sender_email
        or sender_email.count('@') != 1
        or any(character.isspace() for character in sender_email)
    ):
        form_message = 'Please check your details and keep your message under 5,000 characters.'
        form_error = True
    else:
        mail_settings = {
            'MAIL_SERVER': os.environ.get('MAIL_SERVER'),
            'MAIL_PORT': os.environ.get('MAIL_PORT'),
            'MAIL_USERNAME': os.environ.get('MAIL_USERNAME'),
            'MAIL_PASSWORD': os.environ.get('MAIL_PASSWORD'),
            'FROM_EMAIL': os.environ.get('FROM_EMAIL'),
            'TO_EMAIL': os.environ.get('TO_EMAIL'),
        }
        configured_settings = [value for value in mail_settings.values() if value]

        if not configured_settings:
            if app.debug:
                app.logger.info('Contact message from %s <%s>:\n%s', name, sender_email, message)
                form_message = 'Thanks for reaching out. Your message was recorded by the local development server.'
            else:
                form_message = 'Email delivery is not configured yet. Please email me directly instead.'
                form_error = True
        elif len(configured_settings) != len(mail_settings):
            app.logger.error('Contact email is not configured: one or more SMTP settings are missing.')
            form_message = 'Email delivery is not configured yet. Please email me directly instead.'
            form_error = True
        else:
            try:
                port = int(mail_settings['MAIL_PORT'])
                email_message = EmailMessage()
                email_message['Subject'] = f'Portfolio contact from {name}'
                email_message['From'] = mail_settings['FROM_EMAIL']
                email_message['To'] = mail_settings['TO_EMAIL']
                email_message['Reply-To'] = sender_email
                email_message.set_content(f'From: {name} <{sender_email}>\n\n{message}')

                if port == 465:
                    with smtplib.SMTP_SSL(
                        mail_settings['MAIL_SERVER'], port, timeout=10,
                        context=ssl.create_default_context(),
                    ) as server:
                        server.login(mail_settings['MAIL_USERNAME'], mail_settings['MAIL_PASSWORD'])
                        server.send_message(email_message)
                else:
                    with smtplib.SMTP(mail_settings['MAIL_SERVER'], port, timeout=10) as server:
                        server.starttls(context=ssl.create_default_context())
                        server.login(mail_settings['MAIL_USERNAME'], mail_settings['MAIL_PASSWORD'])
                        server.send_message(email_message)
                form_message = 'Thanks for reaching out. Your message has been sent.'
            except (OSError, ValueError, smtplib.SMTPException):
                app.logger.exception('Unable to deliver portfolio contact message.')
                form_message = 'Your message could not be sent right now. Please email me directly.'
                form_error = True

    return render_template(
        'contact.html',
        form_message=form_message,
        form_error=form_error,
    )


@app.route('/resume')
def resume():
    return render_template('resume.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
