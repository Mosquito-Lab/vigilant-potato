from PySide6.QtWidgets import QMenuBar, QMessageBox
from PySide6.QtCore import Slot


# Default class for editors
class TextEditMenuBar(QMenuBar):
    """ Default text edit menu class """

    def __init__(self):
        super().__init__()

        # File menu and does file and window handling
        file_menu = self.addMenu("File")
        file_menu.addAction("New Fie").triggered.connect(self.placeholder)
        file_menu.addAction("New Window").triggered.connect(self.placeholder)
        file_menu.addAction("Open").triggered.connect(self.placeholder)
        file_menu.addAction("Save").triggered.connect(self.placeholder)
        file_menu.addAction("Save As").triggered.connect(self.placeholder)
        file_menu.addSeparator()
        file_menu.addAction("Exit").triggered.connect(self.close)


        # Edit menu that manipulates actions
        edit_menu = self.addMenu("Edit")
        edit_menu.addAction("Cut").triggered.connect(self.placeholder)
        edit_menu.addAction("Copy").triggered.connect(self.placeholder)
        edit_menu.addAction("Paste").triggered.connect(self.placeholder)
        edit_menu.addSeparator()
        edit_menu.addAction("Undo").triggered.connect(self.placeholder)
        edit_menu.addAction("Redo").triggered.connect(self.placeholder)
        edit_menu.addSeparator()
        edit_menu.addAction("Delete").triggered.connect(self.placeholder)

        # View menu that controls the feel
        view_menu = self.addMenu("View")
        view_menu.addAction("Adjust").triggered.connect(self.placeholder)
        view_menu.addAction("Analyze").triggered.connect(self.placeholder)

    @Slot()
    def placeholder(self):
        """ Placeholder method for a default object """


        message = QMessageBox()
        message.setWindowTitle("Default title")
        message.setText("This is a placeholder text")
        message.exec()
