"""
Help on module main:

NAME
    main - This module runs application.
"""

import sys

from PyQt6.QtWidgets import QApplication
from gui import ChatBotWindow


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = ChatBotWindow()
    sys.exit(app.exec())
