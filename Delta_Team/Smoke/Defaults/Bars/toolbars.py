from PySide6.QtWidgets import QToolBar
from PySide6.QtCore import Qt, QSize, Signal
from PySide6.QtGui import QActionGroup

from Delta_Team.Smoke.Defaults.Actions.actions import NavigationAction
from Delta_Team.Images.image_finder import get_image


class NavigationToolBar(QToolBar):
    """
    Modern navigation toolbar for switching between application views.

    This toolbar provides a clean, vertical navigation system with icons
    and text labels. Actions are mutually exclusive (only one can be
    active at a time) and emit signals when clicked to trigger view changes.

    Signals:
        view_changed (str): Emitted when a navigation action is clicked,
                           carries the widget_name identifier

    Features:
        - Vertical orientation on the left side
        - Icon + text button style
        - Mutually exclusive action selection
        - Clean, modern appearance
    """

    # Signal emitted when user clicks a navigation item
    view_changed = Signal(str)

    def __init__(self, parent=None):
        """
        Initialize the navigation toolbar.

        Creates navigation actions for Home, Search, Options, and Settings views.
        Sets up visual styling and connects signals.

        Args:
            parent: Parent widget
        """
        super().__init__(parent)

        # Configure toolbar appearance
        self.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
        self.setIconSize(QSize(32, 32))
        self.setOrientation(Qt.Orientation.Vertical)
        self.setMovable(False)  # Keep toolbar fixed in place

        # Set modern styling
        self.setStyleSheet("""
            QToolBar {
                background-color: #2b2b2b;
                border-right: 1px solid #3d3d3d;
                spacing: 8px;
                padding: 10px;
            }
            QToolButton {
                color: #ffffff;
                background-color: transparent;
                border: none;
                border-radius: 6px;
                padding: 10px;
                font-size: 13px;
                text-align: left;
            }
            QToolButton:hover {
                background-color: #3d3d3d;
            }
            QToolButton:checked {
                background-color: #0d7377;
                font-weight: bold;
            }
        """)

        # Create action group for mutually exclusive selection
        self.action_group = QActionGroup(self)
        self.action_group.setExclusive(True)

        # Create navigation actions
        self._create_actions()

    def _create_actions(self):
        """
        Create and configure all navigation actions.

        Defines the main navigation items: Home, Search, Options, and Settings.
        Each action is added to the action group and connected to the signal handler.
        """
        # Home/Startup action
        home_action = NavigationAction(
            "Home",
            "startup",
            parent=self
        )
        home_action.setChecked(True)  # Start with home selected

        # Search action
        search_action = NavigationAction(
            "Search",
            "search",
            parent=self
        )

        # Options/Download settings action
        options_action = NavigationAction(
            "Download Options",
            "options",
            parent=self
        )

        # Settings action (placeholder for future features)
        settings_action = NavigationAction(
            "Settings",
            "settings",
            parent=self
        )

        # Add all actions to the group and toolbar
        actions = [home_action, search_action, options_action, settings_action]

        for action in actions:
            self.action_group.addAction(action)
            self.addAction(action)
            # Connect each action to emit view_changed signal
            action.triggered.connect(lambda checked, a=action: self._on_action_triggered(a))

        # Add spacer at bottom to push actions to top
        spacer = QToolBar(self)
        spacer.setStyleSheet("background-color: transparent; border: none;")
        self.addWidget(spacer)

    def _on_action_triggered(self, action: NavigationAction):
        """
        Handle navigation action clicks.

        Emits the view_changed signal with the widget identifier
        so the main window can switch to the appropriate view.

        Args:
            action (NavigationAction): The action that was triggered
        """
        self.view_changed.emit(action.widget_name)


class DefaultToolBar(QToolBar):
    """
    Legacy toolbar class maintained for backward compatibility.

    This is the original toolbar implementation. Consider using
    NavigationToolBar for new development.
    """

    def __init__(self):
        super().__init__()

        self.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
        self.setIconSize(QSize(48, 48))
        self.setOrientation(Qt.Orientation.Vertical)