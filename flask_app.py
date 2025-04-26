from flask import Flask, render_template, request, redirect, flash, url_for
from flask_mail import Mail, Message

app = Flask(__name__)
app.secret_key = 'your-secret-key'  # Replace this with a real secret key

# --- Mail Configuration ---
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'notjctingib@gmail.com'  # Replace with your email
app.config['MAIL_PASSWORD'] = 'JesusisGod07'      # Use an app-specific password
app.config['MAIL_DEFAULT_SENDER'] = 'notjctingib@gmail.com'

mail = Mail(app)

# --- Routes ---

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/sermons')
def sermons():
    return render_template('sermons.html')

@app.route('/ministries')
def ministries():
    return render_template('ministries.html')

@app.route('/events')
def events():
    return render_template('events.html')

@app.route('/connect')
def connect():
    return render_template('connect.html')

@app.route('/submit_prayer', methods=['POST'])
def submit_prayer():
    name = request.form.get('name')
    email = request.form.get('email')
    prayer = request.form.get('prayer')

    subject = f"New Prayer Request from {name}"
    body = f"""
    Name: {name}
    Email: {email if email else 'Not provided'}

    Prayer Request:
    {prayer}
    """

    try:
        msg = Message(subject, recipients=['notjctingib@gmail.com'], body=body)
        mail.send(msg)
        flash('Thank you! Your prayer request has been submitted.', 'success')
    except Exception as e:
        print("EMAIL ERROR:", e)
        flash('There was an error sending your request. Please try again later.', 'error')

    return redirect(url_for('connect'))

@app.route("/giving")
def giving():
    return render_template("giving.html")

@app.route("/visit")
def visit():
    return render_template("visit.html")



if __name__ == '__main__':
    app.run(debug=True)
