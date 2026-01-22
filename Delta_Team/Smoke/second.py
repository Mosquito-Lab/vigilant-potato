from pathlib import Path

from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QAction, QIcon
from PySide6.QtWidgets import QApplication, QMainWindow, QToolBar

App = QApplication()
icon_path = Path(__file__).resolve().parent / "Cyber-Smoke077.png"

class MainWindow(QMainWindow):
    title: str
    def __init__(self, title= "Smoke"):
        super().__init__()

        icon = QIcon(str(icon_path))

        self.setWindowTitle(title)
        self.setMinimumSize(600, 400)
        self.setWindowIcon(icon)

        toolbar = QToolBar(
            "Main toolbar", movable=True, orientation=Qt.Orientation.Vertical,
            iconSize=QSize(20, 20)
        )
        self.addToolBar(toolbar)

        commit_action = QAction(icon, "Commit")
        commit_action.setToolTip("Commit")
        commit_action.setShortcut("Ctrl+C")
        toolbar.addAction(commit_action)
        toolbar.addSeparator()
        toolbar.addAction(icon, "Exit").triggered.connect(App.quit)





window = MainWindow()
window.show()
App.exec()