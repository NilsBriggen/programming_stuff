import sys
from PyQt6.QtWidgets import QApplication, QWidget

app = QApplication(sys.argv)
w = QWidget()
w.resize(1080, 720)
w.setWindowTitle("Hallo Silas")
w.show()
app.exec()