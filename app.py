from flask import Flask, request, render_template, redirect, url_for
import smtplib
from email.message import EmailMessage

app = Flask(__name__)

# Email setup
sender_email = 'cryptowatcher2023@gmail.com'
app_key = 'your_app_password_here'

def send_email(to_email, subject, body):
    msg = EmailMessage()
    msg.set_content(body)
    msg['From'] = sender_email
    msg['To'] = to_email
    msg['Subject'] = subject

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email, app_key)
    server.send_message(msg)
    server.quit()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/subscribe', methods=['POST'])
def subscribe():
    email = request.form['email']
    cryptos = request.form.getlist('cryptos')
    if not email or not cryptos:
        return "Missing required fields", 400

    subject = "Crypto Price Updates Subscription"
    body = f"You have subscribed to updates for: {', '.join(cryptos)}"
    
    send_email(email, subject, body)
    return "Subscription successful!", 200

if __name__ == '__main__':
    app.run(debug=True)
