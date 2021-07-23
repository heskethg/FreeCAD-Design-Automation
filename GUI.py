import FreeCAD
import FreeCADGUI
import Part

import sys

from Pyside.Qtwidgets import QApplication

if __name__ == "__main__":
    app = QApplication(sys.argv)
    FreeCADGui.showMainWindow()
    
    doc = FreeCAD.newDocument()
    box = Part.makeBox(100, 100, 100)
    Part.show(box)
    sys.exit(app.exec_())