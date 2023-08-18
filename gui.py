"""
Help on module gui:

NAME
    gui - This module provides a class for building AI chat bot user interface.

The module contains the following class:
- `ChatBotWindow() - This class is inherited from class QMainWindow
and provides the main application window.`
"""

import threading

from PyQt6.QtWidgets import QLineEdit, QMainWindow, QPushButton, QTextEdit

from bot import ChatBot


class ChatBotWindow(QMainWindow):
    """
    This class is inherited from class QMainWindow and provides the main application window.

    Methods
    -------
    get_bot_response(user_input)
        Receive OpenAI's response and add it to the main gui window.
    send_message()
        Send user input via gui window to OpenAI's api.
    """
    def __init__(self):
        super().__init__()

        self.chatbot: ChatBot = ChatBot()
        self.setMinimumSize(700, 500)

        # Widgets
        # chat area widget
        self.chat_area = QTextEdit(self)
        self.chat_area.setGeometry(10, 10, 480, 320)
        self.chat_area.setReadOnly(True)

        # input field widget
        self.input_field = QLineEdit(self)
        self.input_field.setGeometry(10, 340, 480, 40)
        self.input_field.returnPressed.connect(self.send_message)

        # "Send" button widget
        self.button = QPushButton("Send", self)
        self.button.setGeometry(10, 380, 480, 40)
        self.button.clicked.connect(self.send_message)

        self.show()

    def get_bot_response(self, user_input: str) -> None:
        """
        Receive OpenAI's api text response and add it to the chat area in the main gui window.

        Args:
            user_input: A string text that represents user input

        Returns:
            This method does not return anything. It styles a bit gui's output message,
            that basically is a response for user input message.
        """
        response = self.chatbot.get_api_response(user_input)
        self.chat_area.append(
            f"<p style='color:#ffffff; backgound-color:#E9E9E9'>Bot: {response}</p>"
        )

    def send_message(self) -> None:
        """
        Send user input via gui window to OpenAI's api.

        Method extracts user input text from gui's input field,
        displays it's styled version in the main gui window in
        a thread by separating flow of input/output processing execution.
        """
        user_input = self.input_field.text().strip()
        self.chat_area.append(f"<p style='color:#999999'>Me: {user_input}</p>")
        self.input_field.clear()

        thread = threading.Thread(target=self.get_bot_response, args=(user_input,))
        thread.start()
