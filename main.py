import sys
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QTextEdit, QPushButton, QVBoxLayout, QWidget


class EmailApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Create widgets
        self.to_label = QLabel('Recipient Address', self)
        self.subject_label = QLabel('Subject', self)
        self.message_label = QLabel('Message', self)

        self.to_line_edit = QLineEdit(self)
        self.subject_line_edit = QLineEdit(self)
        self.message_text_edit = QTextEdit(self)

        self.send_button = QPushButton('Send', self)
        self.send_button.clicked.connect(self.send_email)  # Connect the button's click event

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.to_label)
        layout.addWidget(self.to_line_edit)
        layout.addWidget(self.subject_label)
        layout.addWidget(self.subject_line_edit)
        layout.addWidget(self.message_label)
        layout.addWidget(self.message_text_edit)
        layout.addWidget(self.send_button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        # Window settings
        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('Send Email')
        self.show()

    def send_email(self):
        # Get the entered email details
        recipient = self.to_line_edit.text()
        subject = self.subject_line_edit.text()
        message = self.message_text_edit.toPlainText()

        # Send the email
        try:
            send_email(recipient, subject, message)
            print("Email sent successfully")
        except Exception as e:
            print(f"Failed to send email: {e}")


def send_email(to_addr, subject, body):
    # SMTP server configuration
    smtp_server = 'smtp.gmail.com'
    smtp_user = 'xuancanhit99@gmail.com'
    smtp_password = 'kpmyefhtgsfmizjv'

    # Create message
    msg = MIMEMultipart()
    msg['From'] = smtp_user
    msg['To'] = to_addr
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    # Send the message via the SMTP server
    try:
        with smtplib.SMTP(smtp_server, 587) as server:
            server.starttls()
            server.login(smtp_user, smtp_password)
            server.send_message(msg)
    except Exception as e:
        raise e


def main():
    app = QApplication(sys.argv)
    ex = EmailApp()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
