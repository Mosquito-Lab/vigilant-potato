from pathlib import Path

from PySide6.QtCore import QSize
from PySide6.QtGui import QPixmap, QIcon
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, \
    QMessageBox, QSizePolicy

App = QApplication()
logo = Path(__file__).resolve().parent.parent.parent.parent / "Images"/"Main logo.jpg"

class LoginForm(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Login Form")
        self.setFixedSize(400,600)

        vertical_Layout = QVBoxLayout()

        logo_label = QLabel()
        logo_label.setPixmap(QPixmap(str(logo)))
        logo_label.adjustSize()
        logo_label.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)

        username_label = QLabel("Username: ", self)
        edit_username = QLineEdit()
        edit_username.setPlaceholderText("Enter Username")

        password_label = QLabel("Password: ", self)
        edit_pass = QLineEdit()
        edit_pass.setPlaceholderText("Enter Password")

        username_layout = QHBoxLayout()
        username_layout.addWidget(username_label)
        username_layout.addWidget(edit_username)

        password_layout = QHBoxLayout()
        password_layout.addWidget(password_label)
        password_layout.addWidget(edit_pass)

        login_button = QPushButton("Login")
        login_button.clicked.connect(lambda : QMessageBox.warning(self,"Login Error","Invalid user!"))
        login_button.setFixedSize(QSize(48, 48))
        login_button.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.MinimumExpanding)

        vertical_Layout.addWidget(logo_label)
        vertical_Layout.addLayout(username_layout)
        vertical_Layout.addLayout(password_layout)
        vertical_Layout.addWidget(login_button)

        self.setLayout(vertical_Layout)

window = LoginForm()
window.show()
App.setWindowIcon(QIcon(str(logo)))
App.exec()



