from PySide6.QtGui import QIcon, QAction

class DefaultAction(QAction):

    def __init__(self,
                 icon: QIcon = None,
                 name: str = "Default action",
                 tooltip: str = "Default tooltip",
                 shortcut: str = None,
                 default_signal=None, ):
        super().__init__()

        self.setText(name)
        self.setToolTip(tooltip)

        if icon:
            self.setIcon(icon)
        if shortcut:
            self.setShortcut(shortcut)
        if default_signal:
            self.triggered.connect(default_signal)

        else:
            self.triggered.connect(lambda: print("This is a default response!"))
