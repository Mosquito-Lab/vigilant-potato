from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QSizePolicy
from PySide6.QtCore import Qt

from Delta_Team.Smoke.Defaults.Bars import titlebars
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # 1. Hide the real title bar
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)

        main_widget = QWidget()
        layout = QVBoxLayout(main_widget)
        layout.setContentsMargins(0, 0, 0, 0)

        # 2. Add our fake title bar
        title_bar = titlebars.CustomTitleBar(self)
        title_bar.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)

        layout.addWidget(title_bar)

        # 3. Add the rest of your app content
        content = QLabel("Hello 66, this is the app body.")
        content.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(content)

        self.setCentralWidget(main_widget)
        self.resize(400, 300)


App = QApplication()
window = MainWindow()
window.show()
App.exec()