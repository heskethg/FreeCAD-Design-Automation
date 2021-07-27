from PySide2.QtCore import QCoreApplication
import FreeCAD as App
import FreeCADGui as Gui
import Part
import sys

from PySide2.QtWidgets import QApplication, QWidget

if __name__ == "__main__":
    my_app = QApplication([])
    QCoreApplication.setApplicationName("FreeCAD Automation TEST")
    Gui.showMainWindow()
    my_doc = App.newDocument()
    box = Part.makeBox(50, 50, 50)
    Part.show(box)
    sys.exit(my_app.exec_())