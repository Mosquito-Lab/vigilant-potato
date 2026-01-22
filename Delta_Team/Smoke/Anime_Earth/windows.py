from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMainWindow
from PySide6.QtGui import QIcon

from Delta_Team.Images.image_finder import get_image
from Delta_Team.Smoke.Anime_Earth import widgets
from Delta_Team.Smoke.Defaults.Toolbars import toolbars


# Main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowIcon(QIcon(get_image("Main logo.jpg")))

        self.setWindowTitle("Anime Earth")

        self.addToolBar(Qt.ToolBarArea.LeftToolBarArea, toolbars.DefaultToolBar())

        start_up = widgets.OptionsWidget()

        self.setCentralWidget(start_up)


# A secondary window for some reason
class SecondaryWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowIcon(get_image("Secondary logo.jpg"))
        self.setWindowTitle("Anime Earth")



