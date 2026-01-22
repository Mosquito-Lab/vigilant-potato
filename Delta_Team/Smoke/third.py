from pathlib import Path

from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QAction, QIcon
from PySide6.QtWidgets import QApplication, QMainWindow, QToolBar, QWidget, QVBoxLayout, QPushButton

from Delta_Team.Smoke.Defaults.Menubars import menubars

App = QApplication()
icon_path = Path(__file__).resolve().parent / "Cyber-Smoke077.png"

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        icon = QIcon(str(icon_path))

        self.setWindowTitle("Delta Team")
        self.setMinimumSize(QSize(400, 600))

        # Menubar logic
        menubar = menubars.TextEditMenuBar()
        self.setMenuBar(menubar)

        # Toolbar logic
        toolbar = QToolBar(
            "Main toolbar",
            movable=False,
            toolButtonStyle=Qt.ToolButtonStyle.ToolButtonIconOnly,
            orientation=Qt.Orientation.Vertical
        )

        commit_action = QAction(icon, "Commit", self)
        commit_action.setToolTip("Commit")
        commit_action.setShortcut("Ctrl+C")
        commit_action.triggered.connect(lambda : print("Hit the commit button!"))
        toolbar.addAction(commit_action)
        toolbar.addAction(icon, "Exit").triggered.connect(App.quit)
        toolbar.addAction(icon, "Banana")

        toolbar.setIconSize(QSize(48, 48))
        self.addToolBar(Qt.ToolBarArea.LeftToolBarArea, toolbar)

        main_widget = QWidget()

        main_widget.setLayout(QVBoxLayout())
        main_widget.layout().addWidget(QPushButton("Banana"))
        self.setCentralWidget(main_widget)


window = MainWindow()
window.show()
App.exec()



