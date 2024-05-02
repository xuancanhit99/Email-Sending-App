from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QPushButton, QVBoxLayout, QWidget, QFileDialog, \
    QFontComboBox, QSpinBox
from PyQt5.QtGui import QFont


# Define the TextEditor class which inherits from QMainWindow
class TextEditor(QMainWindow):
    def __init__(self):
        super().__init__()

        # Create the text editor and buttons
        self.text_edit = QTextEdit()
        self.new_button = QPushButton('New')
        self.open_button = QPushButton('Open')
        self.save_button = QPushButton('Save')

        # Create the font selector and size selector
        self.font_combo_box = QFontComboBox()
        self.font_size_spin_box = QSpinBox()
        self.font_size_spin_box.setRange(1, 100)
        self.font_size_spin_box.setValue(12)

        # Connect the buttons and selectors to their respective functions
        self.new_button.clicked.connect(self.new_file)
        self.open_button.clicked.connect(self.open_file)
        self.save_button.clicked.connect(self.save_file)
        self.font_combo_box.currentFontChanged.connect(self.change_font)
        self.font_size_spin_box.valueChanged.connect(self.change_font_size)

        # Create the layout and add the widgets
        layout = QVBoxLayout()
        layout.addWidget(self.new_button)
        layout.addWidget(self.open_button)
        layout.addWidget(self.save_button)
        layout.addWidget(self.font_combo_box)
        layout.addWidget(self.font_size_spin_box)
        layout.addWidget(self.text_edit)

        # Set the layout in a container and set it as the central widget
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        # Set the initial size of the window
        self.resize(800, 600)

    # Define the function to clear the text editor
    def new_file(self):
        self.text_edit.clear()

    # Define the function to open a file and display its content in the text editor
    def open_file(self):
        file_name, _ = QFileDialog.getOpenFileName(self, 'Open File')
        if file_name:
            with open(file_name, 'r') as file:
                self.text_edit.setText(file.read())

    # Define the function to save the content of the text editor to a file
    def save_file(self):
        file_name, _ = QFileDialog.getSaveFileName(self, 'Save File')
        if file_name:
            with open(file_name, 'w') as file:
                file.write(self.text_edit.toPlainText())

    # Define the function to change the font of the text in the text editor
    def change_font(self, font):
        self.text_edit.setFont(font)

    # Define the function to change the size of the font in the text editor
    def change_font_size(self, size):
        font = self.text_edit.font()
        font.setPointSize(size)
        self.text_edit.setFont(font)


# Run the application
if __name__ == '__main__':
    app = QApplication([])
    editor = TextEditor()
    editor.show()
    app.exec_()
