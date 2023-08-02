import sys

from PyQt6.QtWidgets import (
    QApplication,
    QLineEdit,
    QMainWindow,
    QPushButton,
    QTextEdit
)


class ChatBotWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setMinimumSize(700, 500)

        # Widgets
        # chat area widget
        self.chat_area = QTextEdit(self)
        self.chat_area.setGeometry(10, 10, 480, 320)
        self.chat_area.setReadOnly(True)

        # input field widget
        self.input_area = QLineEdit(self)
        self.input_area.setGeometry(10, 340, 480, 40)

        # button widget
        self.button = QPushButton("Send", self)
        self.button.setGeometry(10, 380, 480, 40)

        self.show()


class ChatBot:
    ...


app = QApplication(sys.argv)
main_window = ChatBotWindow()
sys.exit(app.exec())
