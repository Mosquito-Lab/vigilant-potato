from PySide6.QtWidgets import QWidgetAction
from PySide6.QtGui import QIcon, QAction
from PySide6.QtCore import Signal


class NavigationAction(QAction):
    """
    Custom action for toolbar navigation.

    This action is used to switch between different widgets in the main window.
    Each action represents a specific view/widget (Home, Search, Options, etc.)

    Attributes:
        widget_name (str): Identifier for which widget this action should display

    Signals:
        triggered: Emitted when the action is clicked, carries the widget_name
    """

    def __init__(self, text: str, widget_name: str, icon_path: str = None, parent=None):
        """
        Initialize a navigation action.

        Args:
            text (str): Display text for the action
            widget_name (str): Internal identifier for the target widget
            icon_path (str, optional): Path to icon image file
            parent: Parent QObject
        """
        super().__init__(text, parent)
        self.widget_name = widget_name

        if icon_path:
            self.setIcon(QIcon(icon_path))

        # Make the action checkable for visual feedback
        self.setCheckable(True)


class DefaultAction(QAction):
    """
    Placeholder action for toolbar demonstration.

    This is a simple action that can be used as a template
    or replaced with specific functionality.
    """

    def __init__(self, text: str = "Action", parent=None):
        """
        Initialize a default action.

        Args:
            text (str): Display text for the action
            parent: Parent QObject
        """
        super().__init__(text, parent)
        self.setCheckable(True)