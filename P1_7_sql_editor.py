import sys
import sqlite3
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QTextEdit, QFileDialog, QLabel


class SQLiteManager(QMainWindow):
    def __init__(self):
        super().__init__()

        self.conn = None
        self.initUI()

    def initUI(self):
        # This method initializes the user interface of the SQLiteManager application.
        self.setWindowTitle('SQLite Database Manager')
        self.setGeometry(100, 100, 800, 600)  # Set initial size

        layout = QVBoxLayout()

        # Button to open a database file
        self.btn_open = QPushButton('Open SQLite File', self)
        self.btn_open.clicked.connect(self.open_file_dialog)
        layout.addWidget(self.btn_open)

        # Label for connection status
        self.connection_status = QLabel('No database connected', self)
        layout.addWidget(self.connection_status)

        # Text Edit for SQL Command
        self.sql_command = QTextEdit(self)
        self.sql_command.setPlaceholderText('Enter your SQL command here...')
        layout.addWidget(self.sql_command)

        # Button to Execute Command
        self.btn_execute = QPushButton('Execute Command', self)
        self.btn_execute.clicked.connect(self.execute_command)
        layout.addWidget(self.btn_execute)

        # Text Edit for Result
        self.result_text = QTextEdit(self)
        self.result_text.setReadOnly(True)
        layout.addWidget(self.result_text)

        # Setting the central widget
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def open_file_dialog(self):
        # This method opens a file dialog for the user to select a SQLite database file to connect to.
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file_name, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "",
                                                   "SQLite Files (*.sqlite);;All Files (*)", options=options)
        if file_name:
            self.connect_to_database(file_name)
            self.connection_status.setText(f'Connected to database: {file_name}')

    def connect_to_database(self, db_path):
        # This method establishes a connection to the SQLite database at the specified path.
        try:
            self.conn = sqlite3.connect(db_path)
            self.result_text.setText("Connected to the database successfully.")
        except Exception as e:
            self.result_text.setText("Error: " + str(e))

    def execute_command(self):
        # This method executes the SQL command entered by the user in the sql_command text edit field.
        command = self.sql_command.toPlainText()
        if command.lower() == "clear":
            self.result_text.clear()
        elif command.lower().startswith("select"):
            self.run_query(command)
        else:
            self.run_action(command)

    def run_query(self, query):
        # This method executes a SQL query and displays the results in the result_text text edit field.
        cursor = self.conn.cursor()
        try:
            cursor.execute(query)
            results = cursor.fetchall()
            self.result_text.append("\nResults:")
            for row in results:
                self.result_text.append(str(row))
        except Exception as e:
            self.result_text.append("Error: " + str(e))

    def run_action(self, action):
        # This method executes a SQL action (non-query command) and displays the result in the result_text text edit f
        cursor = self.conn.cursor()
        try:
            cursor.execute(action)
            self.conn.commit()
            self.result_text.append("Action executed successfully.")
        except Exception as e:
            self.result_text.append("Error: " + str(e))



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = SQLiteManager()
    ex.show()
    sys.exit(app.exec_())
