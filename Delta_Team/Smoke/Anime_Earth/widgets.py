from PySide6.QtWidgets import (QWidget, QGridLayout, QLabel, QRadioButton, QPushButton,
                               QGroupBox, QHBoxLayout, QVBoxLayout, QLineEdit, QScrollArea, QFrame)
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt, Signal

from Delta_Team.Images.image_finder import get_image


class StartupWidget(QWidget):
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
        self.main_layout = QVBoxLayout()
        self.main_layout.setContentsMargins(40, 40, 40, 40)
        self.main_layout.setSpacing(30)

        # Add top spacer for vertical centering
        self.main_layout.addStretch(1)

        self.set_central_label(icon=get_image('Cyber-Smoke077.png'))

        # Title label
        title_label = QLabel("Choose Your Destiny")
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title_label.setStyleSheet("font-size: 20px; color: #ffffff; margin: 20px;")
        self.main_layout.addWidget(title_label)

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

        self.main_layout.addWidget(buttons_container)

        # Add bottom spacer for vertical centering
        self.main_layout.addStretch(1)

        self.setLayout(self.main_layout)

    def set_central_label(self, icon: str = None, default_text: str = 'ANIME EARTH'):
        """ Sets an image or text as the central label. """

        # Logo section
        logo_container = QWidget()
        logo_layout = QVBoxLayout(logo_container)
        logo_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        animee_label = QLabel()

        pixmap = QPixmap(icon)

        # Handle if there is a valid image
        if not pixmap.isNull():
            # Scale logo responsively
            scaled_pixmap = pixmap.scaled(
                400, 400, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation
            )
            animee_label.setPixmap(scaled_pixmap)

        else:
            animee_label.setText(default_text)

            animee_label.setStyleSheet("font-size: 48px; color: #0d7377; font-weight: bold;")

        animee_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        logo_layout.addWidget(animee_label)

        self.main_layout.addWidget(logo_container)



class OptionsWidget(QWidget):
    """
    Comprehensive download options configuration widget.

    Provides a detailed interface for users to customize their download
    preferences including quality, language, episode selection, and
    folder naming conventions.

    Features:
        - Quality selection (1080p, 720p, 480p, 360p)
        - Language options (Dubbed, Subbed, Chinese)
        - Episode range or full download
        - Custom folder naming toggle
        - Scrollable interface for smaller screens
        - Organized into logical groups

    Methods:
        get_selected_quality(): Returns selected quality string
        get_selected_language(): Returns selected language string
        get_episode_mode(): Returns episode download mode
        use_default_folder_name(): Returns boolean for folder naming preference
    """

    def __init__(self, parent=None):
        """
        Initialize the 'options' widget.

        Creates all option groups and configures their layouts
        with proper styling and organization.

        Args:
            parent: Parent widget
        """
        super().__init__(parent)

        # Create scroll area for better responsiveness
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setFrameShape(QFrame.Shape.NoFrame)
        scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)

        # Container widget for scroll area
        container = QWidget()

        # Configure styling
        self.setStyleSheet("""
            QWidget {
                background-color: #1e1e1e;
                color: #ffffff;
            }
            QGroupBox {
                background-color: #2b2b2b;
                border: 2px solid #3d3d3d;
                border-radius: 8px;
                margin-top: 12px;
                padding: 15px;
                font-weight: bold;
                font-size: 14px;
            }
            QGroupBox::title {
                subcontrol-origin: margin;
                subcontrol-position: top center;
                padding: 0 10px;
                color: #0d7377;
            }
            QRadioButton {
                spacing: 8px;
                padding: 5px;
            }
            QRadioButton::indicator {
                width: 18px;
                height: 18px;
            }
            QRadioButton::indicator:unchecked {
                border: 2px solid #5d5d5d;
                border-radius: 9px;
                background-color: #2b2b2b;
            }
            QRadioButton::indicator:checked {
                border: 2px solid #0d7377;
                border-radius: 9px;
                background-color: #0d7377;
            }
            QRadioButton:hover {
                color: #14a085;
            }
        """)

        # Title
        title = QLabel("Download Options")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setStyleSheet("font-size: 24px; font-weight: bold; margin: 20px; color: #ffffff;")

        # QUALITY OPTIONS
        quality_group = QGroupBox("Video Quality")
        self.q1 = QRadioButton("1080p (Full HD)")
        self.q2 = QRadioButton("720p (HD) - Recommended")
        self.q2.setChecked(True)
        self.q3 = QRadioButton("480p (SD)")
        self.q4 = QRadioButton("360p (Low)")

        quality_layout = QVBoxLayout()
        quality_layout.addWidget(self.q1)
        quality_layout.addWidget(self.q2)
        quality_layout.addWidget(self.q3)
        quality_layout.addWidget(self.q4)
        quality_group.setLayout(quality_layout)

        # LANGUAGE OPTIONS
        language_group = QGroupBox("Audio & Subtitles")
        self.dubbed = QRadioButton("Dubbed (English Audio)")
        self.subbed = QRadioButton("Subbed (Original Audio + Subtitles)")
        self.subbed.setChecked(True)
        self.chinese = QRadioButton("Chinese (Mandarin)")

        language_layout = QVBoxLayout()
        language_layout.addWidget(self.dubbed)
        language_layout.addWidget(self.subbed)
        language_layout.addWidget(self.chinese)
        language_group.setLayout(language_layout)

        # EPISODES OPTIONS
        episodes_group = QGroupBox("Episode Selection")
        self.download_all = QRadioButton("Download All Episodes")
        self.download_all.setChecked(True)
        self.range_selector = QRadioButton("Download Specific Range")

        episodes_layout = QVBoxLayout()
        episodes_layout.addWidget(self.download_all)
        episodes_layout.addWidget(self.range_selector)
        episodes_group.setLayout(episodes_layout)

        # FOLDER NAME OPTIONS
        folder_group = QGroupBox("Folder Naming")
        folder_label = QLabel("Use the default folder name as shown on the website?")
        folder_label.setWordWrap(True)
        folder_label.setStyleSheet("color: #cccccc; font-weight: normal; margin-bottom: 10px;")
        self.folder_yes = QRadioButton("Yes - Use default name")
        self.folder_yes.setChecked(True)
        self.folder_no = QRadioButton("No - I'll specify a custom name")

        folder_layout = QVBoxLayout()
        folder_layout.addWidget(folder_label)
        folder_layout.addWidget(self.folder_yes)
        folder_layout.addWidget(self.folder_no)
        folder_group.setLayout(folder_layout)

        # MAIN LAYOUT
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(30, 20, 30, 20)
        main_layout.setSpacing(20)

        main_layout.addWidget(title)

        # Grid for organized display
        grid = QGridLayout()
        grid.setSpacing(15)
        grid.addWidget(quality_group, 0, 0)
        grid.addWidget(language_group, 0, 1)
        grid.addWidget(episodes_group, 1, 0)
        grid.addWidget(folder_group, 1, 1)

        main_layout.addLayout(grid)
        main_layout.addStretch()

        container.setLayout(main_layout)
        scroll.setWidget(container)

        # Final layout
        final_layout = QVBoxLayout()
        final_layout.setContentsMargins(0, 0, 0, 0)
        final_layout.addWidget(scroll)
        self.setLayout(final_layout)

    def get_selected_quality(self) -> str:
        """Get the currently selected video quality."""
        if self.q1.isChecked():
            return "1080p"
        elif self.q2.isChecked():
            return "720p"
        elif self.q3.isChecked():
            return "480p"
        else:
            return "360p"

    def get_selected_language(self) -> str:
        """Get the currently selected language/audio option."""
        if self.dubbed.isChecked():
            return "dubbed"
        elif self.subbed.isChecked():
            return "subbed"
        else:
            return "chinese"

    def get_episode_mode(self) -> str:
        """Get the episode download mode (all or range)."""
        return "all" if self.download_all.isChecked() else "range"

    def use_default_folder_name(self) -> bool:
        """Check if user wants to use default folder naming."""
        return self.folder_yes.isChecked()


class SearchWidget(QWidget):
    """
    Advanced search interface for finding anime/animation content.

    Provides a comprehensive search system with multiple handler modes
    and exact name matching options. Allows users to search for content
    and specify how they want the search to be processed.

    Signals:
        search_requested (str, bool, str): Emitted when search button clicked
                                          Args: (search_term, is_exact, handler_mode)

    Features:
        - Text input with placeholder guidance
        - Exact name matching toggle
        - Multiple handler modes (Simple, Complex, Choice)
        - Clean, modern search interface
        - Real-time validation feedback

    Handler Modes:
        - Simple: Basic search algorithm (fastest)
        - Complex: Advanced search with filtering
        - Choice: Interactive selection from results
    """

    search_requested = Signal(str, bool, str)

    def __init__(self, parent=None):
        """
        Initialize the search widget.

        Creates the search input, configuration options, and
        search button with proper styling and connections.

        Args:
            parent: Parent widget
        """
        super().__init__(parent)

        # Configure styling
        self.setStyleSheet("""
            QWidget {
                background-color: #1e1e1e;
                color: #ffffff;
            }
            QLineEdit {
                background-color: #2b2b2b;
                border: 2px solid #3d3d3d;
                border-radius: 6px;
                padding: 12px;
                font-size: 14px;
                color: #ffffff;
            }
            QLineEdit:focus {
                border: 2px solid #0d7377;
            }
            QGroupBox {
                background-color: #2b2b2b;
                border: 2px solid #3d3d3d;
                border-radius: 8px;
                margin-top: 12px;
                padding: 15px;
                font-weight: bold;
                font-size: 13px;
            }
            QGroupBox::title {
                subcontrol-origin: margin;
                subcontrol-position: top left;
                padding: 0 10px;
                color: #0d7377;
            }
            QRadioButton {
                spacing: 8px;
                padding: 8px;
            }
            QRadioButton::indicator {
                width: 18px;
                height: 18px;
            }
            QRadioButton::indicator:unchecked {
                border: 2px solid #5d5d5d;
                border-radius: 9px;
                background-color: #2b2b2b;
            }
            QRadioButton::indicator:checked {
                border: 2px solid #0d7377;
                border-radius: 9px;
                background-color: #0d7377;
            }
            QPushButton {
                background-color: #0d7377;
                color: white;
                border: none;
                border-radius: 8px;
                padding: 15px 40px;
                font-size: 15px;
                font-weight: bold;
                min-height: 50px;
            }
            QPushButton:hover {
                background-color: #14a085;
            }
            QPushButton:pressed {
                background-color: #0a5f62;
            }
            QLabel {
                color: #cccccc;
            }
        """)

        # Main layout
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(40, 40, 40, 40)
        main_layout.setSpacing(25)

        # Title
        title = QLabel("Search for Content")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setStyleSheet("font-size: 26px; font-weight: bold; color: #ffffff; margin-bottom: 10px;")
        main_layout.addWidget(title)

        # Search input section
        search_section = QWidget()
        search_layout = QVBoxLayout(search_section)
        search_layout.setSpacing(10)

        name_label = QLabel("Enter the name of the anime or animation:")
        name_label.setStyleSheet("font-size: 14px; font-weight: bold;")

        self.edit_name = QLineEdit()
        self.edit_name.setPlaceholderText("e.g., Attack on Titan Season 3, Demon Slayer...")
        self.edit_name.returnPressed.connect(self._perform_search)

        search_layout.addWidget(name_label)
        search_layout.addWidget(self.edit_name)
        main_layout.addWidget(search_section)

        # Options section
        options_container = QWidget()
        options_layout = QHBoxLayout(options_container)
        options_layout.setSpacing(15)

        # EXACT NAME OPTIONS
        exact_group = QGroupBox("Name Matching")
        exact_info = QLabel("Is the name exact?\n(Season and all, word for word)")
        exact_info.setWordWrap(True)
        exact_info.setStyleSheet("color: #999999; font-weight: normal; font-size: 12px;")

        self.exact_yes = QRadioButton("Yes - Exact match")
        self.exact_no = QRadioButton("No - Fuzzy search")
        self.exact_no.setChecked(True)

        exact_layout = QVBoxLayout()
        exact_layout.addWidget(exact_info)
        exact_layout.addWidget(self.exact_yes)
        exact_layout.addWidget(self.exact_no)
        exact_layout.addStretch()
        exact_group.setLayout(exact_layout)

        # HANDLER OPTIONS
        handler_group = QGroupBox("Search Handler")
        handler_info = QLabel("Choose search algorithm:")
        handler_info.setStyleSheet("color: #999999; font-weight: normal; font-size: 12px;")

        self.handler_simple = QRadioButton("Simple (Fast)")
        self.handler_simple.setChecked(True)
        self.handler_complex = QRadioButton("Complex (Thorough)")
        self.handler_choice = QRadioButton("Choice (Interactive)")

        handler_layout = QVBoxLayout()
        handler_layout.addWidget(handler_info)
        handler_layout.addWidget(self.handler_simple)
        handler_layout.addWidget(self.handler_complex)
        handler_layout.addWidget(self.handler_choice)
        handler_layout.addStretch()
        handler_group.setLayout(handler_layout)

        options_layout.addWidget(exact_group)
        options_layout.addWidget(handler_group)
        main_layout.addWidget(options_container)

        # Search button
        search_button = QPushButton("🔍 Search")
        search_button.clicked.connect(self._perform_search)
        search_button.setCursor(Qt.CursorShape.PointingHandCursor)
        main_layout.addWidget(search_button)

        # Add stretch to push everything to top
        main_layout.addStretch()

        self.setLayout(main_layout)

    def _perform_search(self):
        """
        Internal method to handle search execution.

        Validates input and emits search_requested signal with
        the search term, exact match flag, and handler mode.
        """
        search_term = self.edit_name.text().strip()

        if not search_term:
            return

        is_exact = self.exact_yes.isChecked()

        if self.handler_simple.isChecked():
            handler = "simple"
        elif self.handler_complex.isChecked():
            handler = "complex"
        else:
            handler = "choice"

        self.search_requested.emit(search_term, is_exact, handler)

    def get_search_term(self) -> str:
        """Get the current search term from input field."""
        return self.edit_name.text().strip()

    def is_exact_match(self) -> bool:
        """Check if exact matching is enabled."""
        return self.exact_yes.isChecked()

    def get_handler_mode(self) -> str:
        """Get the selected handler mode."""
        if self.handler_simple.isChecked():
            return "simple"
        elif self.handler_complex.isChecked():
            return "complex"
        else:
            return "choice"


class SettingsWidget(QWidget):
    """
    Application settings and preferences widget.

    Placeholder widget for future settings functionality such as:
    - Download directory configuration
    - Theme selection
    - Network settings
    - Notification preferences

    This widget can be expanded as needed with additional
    configuration options.
    """

    def __init__(self, parent=None):
        """
        Initialize the settings widget.

        Displays a placeholder message indicating
        this feature is under development.

        Args:
            parent: Parent widget
        """
        super().__init__(parent)

        self.setStyleSheet("""
            QWidget {
                background-color: #1e1e1e;
                color: #ffffff;
            }
            QLabel {
                color: #cccccc;
            }
        """)

        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        title = QLabel("Settings")
        title.setStyleSheet("font-size: 28px; font-weight: bold; color: #ffffff;")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        message = QLabel("Settings panel coming soon!")
        message.setStyleSheet("font-size: 16px; color: #999999; margin-top: 20px;")
        message.setAlignment(Qt.AlignmentFlag.AlignCenter)

        layout.addWidget(title)
        layout.addWidget(message)

        self.setLayout(layout)