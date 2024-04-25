from flask import Flask, request, jsonify
from flask_mail import Mail, Message

app = Flask(__name__)

# Configuration for Flask-Mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = 'xuancanhit99@gmail.com'
app.config['MAIL_PASSWORD'] = 'kpmyefhtgsfmizjv'
app.config['MAIL_DEFAULT_SENDER'] = ('Xuan Canh', 'xuancanhit99@gmail.com')

mail = Mail(app)


# Route decorator defining the endpoint '/send_email' for handling POST requests
@app.route('/send_email', methods=['POST'])
def send_email():
    data = request.json
    subject = data.get('subject')
    sender = data.get('sender')
    recipients = data.get('recipients')
    body = data.get('body')

    if not all([subject, sender, recipients, body]):
        return jsonify({'error': 'Missing data'}), 400

    message = Message(subject, sender=sender, recipients=[recipients], body=body)
    mail.send(message)

    return jsonify({'message': 'Email sent successfully'}), 200


if __name__ == '__main__':
    app.run(debug=True, port=5000)
