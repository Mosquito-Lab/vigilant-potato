from PySide6.QtWidgets import QApplication

from Delta_Team.Smoke.Anime_Earth.windows import MainWindow

# QT API
App = QApplication()

window = MainWindow()
window.show()
App.exec()


