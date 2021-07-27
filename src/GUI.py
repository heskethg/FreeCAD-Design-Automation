import FreeCAD as App
import FreeCADGui as Gui
import Part
import sys

from PySide2.QtWidgets import QApplication

if __name__ == "__main__":
    qapp = QApplication(sys.argv)
    Gui.showMainWindow()
    
    doc = App.newDocument()
    box = Part.makeBox(50, 50, 50)
    Part.show(box)

    sys.exit(qapp.exec_())