from PySide6.QtWidgets import QToolBar
from PySide6.QtCore import Qt, QSize

from Delta_Team.Smoke.Defaults.Actions import actions

class DefaultToolBar(QToolBar):
    def __init__(self):
        super().__init__()

        self.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
        self.setIconSize(QSize(48, 48))
        self.setOrientation(Qt.Orientation.Vertical)


        action_1 = actions.DefaultAction()
        action_2 = actions.DefaultAction()



        self.addAction(action_1)
        self.addAction(action_2)
