from flask import Flask, request, jsonify
from flask_mail import Mail, Message

app = Flask(__name__)


@app.route('/send_email', methods=['POST'])
def send_email():
    data = request.json
    subject = data.get('subject')
    sender = data.get('sender')
    recipients = data.get('recipients')
    body = data.get('body')
    attachment_paths = data.get('attachments')
    mail_server = data.get('mail_server')
    mail_port = data.get('mail_port')
    use_tls = data.get('use_tls')
    mail_username = data.get('mail_username')
    mail_password = data.get('mail_password')

    if not all([subject, sender, recipients, body, mail_server, mail_port, use_tls, mail_username, mail_password]):
        return jsonify({'error': 'Missing data'}), 400

    # Update the Flask-Mail configuration
    app.config['MAIL_SERVER'] = mail_server
    app.config['MAIL_PORT'] = mail_port
    app.config['MAIL_USE_TLS'] = use_tls
    app.config['MAIL_USERNAME'] = mail_username
    app.config['MAIL_PASSWORD'] = mail_password

    # Create a new Flask-Mail instance with the updated configuration
    mail = Mail(app)
    message = Message(subject, sender=sender, recipients=[recipients], body=body)

    if attachment_paths:
        for attachment_path in attachment_paths:
            with app.open_resource(attachment_path) as fp:
                message.attach(attachment_path, "application/octet-stream", fp.read())

    mail.send(message)

    return jsonify({'message': 'Email sent successfully'}), 200


if __name__ == '__main__':
    app.run(debug=True, port=5000)
