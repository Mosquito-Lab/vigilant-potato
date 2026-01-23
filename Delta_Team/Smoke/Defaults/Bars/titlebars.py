from PySide6.QtWidgets import QWidget, QHBoxLayout, QPushButton, QLabel
from PySide6.QtCore import Qt, QPoint
from PySide6.QtGui import QPixmap

from Delta_Team.Images.image_finder import get_image

class CustomTitleBar(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

        window_icon = QLabel("Icon")
        window_icon.setPixmap(QPixmap(get_image('Main logo.jpg')))
        window_icon.resize(window_icon.size())
        window_icon.setFixedSize(30,30)

        titlebar_layout = QHBoxLayout(self)
        titlebar_layout.setContentsMargins(5, 0, 5, 0)

        title = QLabel("My Custom Title Bar")
        btn_close = QPushButton("X")
        btn_close.setFixedSize(30, 30)
        btn_close.clicked.connect(self.parent.close)

        btn_minimize = QPushButton("-")
        btn_minimize.setFixedSize(30, 30)

        btn_maximize = QPushButton("[]")
        btn_maximize.setFixedSize(30, 30)

        titlebar_layout.addWidget(window_icon)
        titlebar_layout.addWidget(title)
        titlebar_layout.addStretch()
        titlebar_layout.addWidget(btn_minimize)
        titlebar_layout.addWidget(btn_maximize)
        titlebar_layout.addWidget(btn_close)

        # Style it (You'd usually use QSS/CSS here)
        self.setStyleSheet("background-color: #333; color: white;")

    # Logic to make the window draggable
    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.parent.old_pos = event.globalPosition().toPoint()

    def mouseMoveEvent(self, event):
        if hasattr(self.parent, 'old_pos'):
            delta = QPoint(event.globalPosition().toPoint() - self.parent.old_pos)
            self.parent.move(self.parent.x() + delta.x(), self.parent.y() + delta.y())
            self.parent.old_pos = event.globalPosition().toPoint()


