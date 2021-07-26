import FreeCAD as App
import FreeCADGui as Gui
import Part
import sys

if __name__ == "__main__":
    myDoc = App.newDocument("Test1")
    App.setActiveDocument("Test1")
    print(App.listDocuments())
    print(App.activeDocument())

    # Gui.showMainWindow()

    box = Part.makeBox(100, 100, 100)
    Part.show(box)

print(sys.version)