from PySide6.QtCore import Qt, QSize, Slot
from PySide6.QtWidgets import QMainWindow, QStackedWidget
from PySide6.QtGui import QIcon

from Delta_Team.Images.image_finder import get_image
from Delta_Team.Smoke.Anime_Earth import widgets
from Delta_Team.Smoke.Defaults.Bars.toolbars import NavigationToolBar


class MainWindow(QMainWindow):
    """
    Main application window with navigation and view switching.

    This is the primary window that houses all application functionality.
    It features a fixed navigation toolbar on the left side and a central
    content area that switches between different widgets based on user
    navigation choices.

    Architecture:
        - Uses QStackedWidget for efficient view switching
        - NavigationToolBar for user navigation
        - Responsive design that adapts to window resizing
        - Modern dark theme throughout

    Available Views:
        - Startup: Initial landing page (Home)
        - Search: Content search interface
        - Options: Download configuration
        - Settings: Application settings (placeholder)

    Attributes:
        toolbar (NavigationToolBar): Left-side navigation toolbar
        stacked_widget (QStackedWidget): Container for switchable views
        widget_map (dict): Maps view names to widget indices
    """

    def __init__(self):
        """
        Initialize the main application window.

        Sets up the window properties, creates all widgets, configures
        the navigation toolbar, and establishes signal connections for
        view switching.
        """
        super().__init__()

        self.setObjectName('MainWindow')
        # Window configuration
        self._setup_window()

        # Create the central widget structure
        self._create_central_widget()

        # Set initial size (responsive, but starts at reasonable dimensions)
        self.resize(1200, 800)
        self.setMinimumSize(QSize(600, 400))

    def _setup_window(self):
        """
        Configure basic window properties.

        Sets window title, icon, and applies the dark theme stylesheet
        to the entire application window.
        """
        # Set window icon
        self.setWindowIcon(QIcon(get_image("Main logo.jpg")))

        self.setWindowTitle("Anime Earth - Downloader")

        # Apply dark theme to main window
        self.setStyleSheet("""
            MainWindow {
                background-color: #1e1e1e;
            }
        """)

    def _create_central_widget(self):
        """
        Create and configure the central widget layout.

        Sets up the navigation toolbar on the left and a stacked widget
        on the right for displaying different views. Connects navigation
        signals to view switching logic.
        """

        # Create navigation toolbar
        self.toolbar = NavigationToolBar(self)
        self.addToolBar(Qt.ToolBarArea.LeftToolBarArea, self.toolbar)

        # Create stacked widget to hold different views
        self.stacked_widget = QStackedWidget()

        # Create and add all widgets
        self.startup_widget = widgets.StartupWidget()
        self.search_widget = widgets.SearchWidget()
        self.options_widget = widgets.OptionsWidget()
        self.settings_widget = widgets.SettingsWidget()

        # Add widgets to stack and create mapping
        self.widget_map = {
            'startup': self.stacked_widget.addWidget(self.startup_widget),
            'search': self.stacked_widget.addWidget(self.search_widget),
            'options': self.stacked_widget.addWidget(self.options_widget),
            'settings': self.stacked_widget.addWidget(self.settings_widget)
        }

        # Set stacked widget as central widget
        self.setCentralWidget(self.stacked_widget)

        # Connect navigation signals
        self.toolbar.view_changed.connect(self._switch_view)

        # Connect startup widget buttons to navigate to relevant views
        self.startup_widget.anime_selected.connect(lambda: self._switch_view('search'))
        self.startup_widget.animation_selected.connect(lambda: self._switch_view('search'))

        # Connect search widget signal (for future implementation)
        self.search_widget.search_requested.connect(self._handle_search)

    @Slot()
    def _switch_view(self, view_name: str):
        """
        Switch to a different view in the stacked widget.

        Changes the currently displayed widget based on the view name
        provided by navigation actions. Updates the central content area
        to show the requested view.

        Args:
            view_name (str): Identifier for the target view
                           ('startup', 'search', 'options', 'settings')
        """

        if view_name in self.widget_map:
            widget_index = self.widget_map[view_name]
            self.stacked_widget.setCurrentIndex(widget_index)

    @Slot()
    def _handle_search(self, search_term: str, is_exact: bool, handler: str):
        """
        Handle search requests from the search widget.

        This is a placeholder for actual search functionality.
        In a complete implementation, this would trigger the download
        search process with the specified parameters.

        Args:
            search_term (str): The search query entered by user
            is_exact (bool): Whether to use exact matching
            handler (str): Search handler mode ('simple', 'complex', 'choice')
        """

        print(f"Search requested: '{search_term}'")
        print(f"Exact match: {is_exact}")
        print(f"Handler: {handler}")

