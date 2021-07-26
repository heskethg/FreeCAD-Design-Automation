""" import sys

from PySide6.QtCore import Qt

from PySide6.QtWidgets import QApplication, QLabel

if __name__ == "__main__":

    app = QApplication(sys.argv)

    label = QLabel("Hello World", alignment=Qt.AlignCenter)

    label.show()

    sys.exit(app.exec_()) """

import FreeCAD
import FreeCADGui
import Part
import sys
from PySide6.QtWidgets import QApplication
if __name__ == "__main__":
    app = QApplication(sys.argv)
    FreeCADGui.showMainWindow()
    doc = FreeCAD.newDocument()
    box = Part.makeBox(100, 100, 100)
    Part.show(box)
    sys.exit(app.exec_())