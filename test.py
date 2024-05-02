import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QFileDialog, QTextEdit
import sqlite3


class DatabaseApp(QMainWindow):
    def __init__(self):
        super().__init__()

        # Create the text editor and buttons
        self.text_edit = QTextEdit()
        self.connect_button = QPushButton('Connect to DB')
        self.query_button = QPushButton('Execute Query')

        # Connect the buttons to their respective functions
        self.connect_button.clicked.connect(self.connect_db)
        self.query_button.clicked.connect(self.execute_query)

        # Create the layout and add the widgets
        layout = QVBoxLayout()
        layout.addWidget(self.connect_button)
        layout.addWidget(self.query_button)
        layout.addWidget(self.text_edit)

        # Set the layout in a container and set it as the central widget
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        # Set the initial size of the window
        self.resize(800, 600)

        self.db_connection = None
        self.cursor = None

    def connect_db(self):
        db_file, _ = QFileDialog.getOpenFileName(self, 'Open DB File')
        if db_file:
            self.db_connection = sqlite3.connect(db_file)
            self.cursor = self.db_connection.cursor()
            self.text_edit.append('Connected to database: {}'.format(db_file))

    def execute_query(self):
        query = self.text_edit.toPlainText()
        if query and self.cursor:
            try:
                self.cursor.execute(query)
                self.db_connection.commit()
                self.text_edit.append('Query executed successfully')
            except Exception as e:
                self.text_edit.append('Failed to execute query: {}'.format(str(e)))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    db_app = DatabaseApp()
    db_app.show()
    sys.exit(app.exec_())