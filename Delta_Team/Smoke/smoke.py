from PySide6.QtGui import QIcon, QPixmap
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QSplashScreen, QLineEdit, QPushButton, QDialog, \
    QWidget, QToolBar

from Delta_Team.Smoke.Defaults.Bars.menubars import TextEditMenuBar
from Delta_Team.Images.image_finder import get_image

App = QApplication()

icon_path = get_image("Cyber-Smoke077.png")
class MainWindow(QMainWindow):
    """ Main window class """

    def __init__(self, window_title = "Default title"):
        super().__init__()

        self.setWindowTitle(window_title)

        menu = TextEditMenuBar() # Call the default text edit menubar


        self.setMenuBar(menu)
        self.setWindowIcon(QIcon(icon_path))
        self.setMinimumSize(600,400)

        main_widget = QWidget()
        main_widget.setLayout(QVBoxLayout())
        login_form = LoginForm()

        self.toolBar = QToolBar()

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
splash.setPixmap(QPixmap(icon_path))
splash.setFixedSize(600,400)
splash.adjustSize()
splash.show()
splash.showMessage("Killer Who? Killer What?", Qt.AlignmentFlag.AlignCenter & Qt.AlignmentFlag.AlignTop)
splash.finish(window)
window.show()
App.exec()