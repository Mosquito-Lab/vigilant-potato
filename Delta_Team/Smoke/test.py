from PySide6.QtWidgets import QApplication, QMessageBox
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader

app = QApplication()

ui = QUiLoader()
file = QFile("qt_designer_test1.ui")
file.readAll()

window = ui.load(file)
file.close()

window.show()
app.exec()