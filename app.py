from flask import Flask, render_template, request
import ai_helper

app = Flask(__name__)

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

@app.route('/resume')
def resume():
    return render_template('resume.html')

@app.route('/ai-assistant', methods=['GET', 'POST'])
def ai_assistant():
    response = None
    prompt = None
    if request.method == 'POST':
        prompt = request.form.get('prompt')
        if prompt:
            # Use the library functions
            raw_response = ai_helper.get_response(prompt)
            response = ai_helper.format_response(raw_response)
    
    return render_template('ai_assistant.html', response=response, prompt=prompt)

if __name__ == "__main__":
    app.run(debug=True)

