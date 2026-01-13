from pathlib import Path
from PySide6.QtGui import QIcon, QPixmap
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QSplashScreen, QLineEdit, QPushButton, QDialog, \
QWidget

from Delta_Team.Smoke.Defaults.Menubars.menubars import TextEditMenuBar

App = QApplication()

icon_path = Path(__file__).resolve().parent / "Cyber-Smoke077.png"

class MainWindow(QMainWindow):
    """ Main window class """

    window_title: str

    def __init__(self, window_title = "Default title"):
        super().__init__()

        self.window_title = window_title
        self.setWindowTitle(window_title)

        menu = TextEditMenuBar() # Call the default text edit menubar


        self.setMenuBar(menu)
        self.setWindowIcon(QIcon(str(icon_path)))
        self.setMinimumSize(600,400)

        main_widget = QWidget()
        main_widget.setLayout(QVBoxLayout())
        login_form = LoginForm()

        main_widget.layout().addWidget(login_form)

        self.setCentralWidget(main_widget)



class LoginForm(QDialog):
    """ Login dialog class """

    def __init__(self):
        super().__init__()

        username = QLineEdit(self)
        password = QLineEdit(self)
        submit = QPushButton("Login")

        layout = QVBoxLayout()
        layout.addWidget(username)
        layout.addWidget(password)
        layout.addWidget(submit)

        self.setLayout(layout)


window = MainWindow("Killer Smoke")
splash = QSplashScreen()
splash.setPixmap(QPixmap(str(icon_path)))
splash.show()
splash.showMessage("Killer Who? Killer What?", Qt.AlignmentFlag.AlignCenter & Qt.AlignmentFlag.AlignTop)
splash.finish(window)
window.show()
App.exec()