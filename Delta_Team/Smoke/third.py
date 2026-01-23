from PySide6.QtWidgets import QWidget, QLabel, QPushButton, QHBoxLayout, QVBoxLayout
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt, Signal

from Delta_Team.Images.image_finder import get_image


class DetailedStartupWidget(QWidget):
    """
    Initial landing page widget for selecting content type.

    This widget serves as the home screen where users choose between
    downloading Anime or Animation content. Features a logo display
    and two large action buttons.

    Signals:
        anime_selected: Emitted when user clicks Anime button
        animation_selected: Emitted when user clicks Animation button

    Features:
        - Centered logo display
        - Two prominent action buttons
        - Responsive layout that adapts to window size
        - Modern card-based design
    """

    anime_selected = Signal()
    animation_selected = Signal()

    def __init__(self, parent=None):
        """
        Initialize the startup widget.

        Creates the logo display and action buttons with proper
        spacing and alignment.

        Args:
            parent: Parent widget
        """
        super().__init__(parent)

        # Configure widget appearance
        self.setStyleSheet("""
            QWidget {
                background-color: #1e1e1e;
            }
            QPushButton {
                background-color: #0d7377;
                color: white;
                border: none;
                border-radius: 8px;
                padding: 20px 40px;
                font-size: 16px;
                font-weight: bold;
                min-width: 200px;
            }
            QPushButton:hover {
                background-color: #14a085;
            }
            QPushButton:pressed {
                background-color: #0a5f62;
            }
        """)

        # Main layout
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(40, 40, 40, 40)
        main_layout.setSpacing(30)

        # Add top spacer for vertical centering
        main_layout.addStretch(1)

        # Logo section
        logo_container = QWidget()
        logo_layout = QVBoxLayout(logo_container)
        logo_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        animee_label = QLabel()

        pixmap = QPixmap(get_image('Cyber-Smoke077.png'))
        if not pixmap.isNull():
            # Scale logo responsively
            scaled_pixmap = pixmap.scaled(400, 400, Qt.AspectRatioMode.KeepAspectRatio,
                                          Qt.TransformationMode.SmoothTransformation)
            animee_label.setPixmap(scaled_pixmap)
        else:
            animee_label.setText("ANIMEE")
            animee_label.setStyleSheet("font-size: 48px; color: #0d7377; font-weight: bold;")

        animee_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        logo_layout.addWidget(animee_label)

        main_layout.addWidget(logo_container)

        # Title label
        title_label = QLabel("Choose Your Content Type")
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title_label.setStyleSheet("font-size: 20px; color: #ffffff; margin: 20px;")
        main_layout.addWidget(title_label)

        # Buttons section
        buttons_container = QWidget()
        buttons_layout = QHBoxLayout(buttons_container)
        buttons_layout.setSpacing(20)
        buttons_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        anime_button = QPushButton("Anime")
        anime_button.clicked.connect(self.anime_selected.emit)

        animation_button = QPushButton("Animation")
        animation_button.clicked.connect(self.animation_selected.emit)

        buttons_layout.addWidget(anime_button)
        buttons_layout.addWidget(animation_button)

        main_layout.addWidget(buttons_container)

        # Add bottom spacer for vertical centering
        main_layout.addStretch(1)

        self.setLayout(main_layout)

