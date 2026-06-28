import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QCheckBox
from PyQt5.QtCore import Qt

# Qt.Checked is just an enum value (2). Comparing the signal's state argument
# against it is how you know whether the box is actually ticked or not.


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # setGeometry(x, y, width, height) places and sizes the window itself,
        # not the widgets inside it. x and y are the top left corner on screen.
        self.setGeometry(700, 300, 500, 500)
        self.setWindowTitle("Checkbox Demo")  # added so the window isn't titleless

        # Passing self as the parent means this checkbox lives inside MainWindow.
        # Without a parent, Qt would treat it as its own standalone top level window.
        self.checkbox = QCheckBox("Do you like food?", self)

        self.initUI()

    def initUI(self):
        # This geometry is relative to the parent (the window), not the screen.
        self.checkbox.setGeometry(10, 0, 500, 100)

        # setStyleSheet works like CSS. Qt widgets understand a subset of CSS
        # properties, font-size and font-family being two common ones.
        self.checkbox.setStyleSheet(
            "font-size: 50px;"
            "font-family: Arial;"
        )

        # This is the signal-slot connection. stateChanged is the signal Qt
        # fires automatically whenever the checkbox is ticked or unticked.
        # connect() tells Qt: whenever that happens, call checkbox_changed for me.
        # You never call checkbox_changed yourself, Qt calls it and passes the
        # new state as the argument.
        self.checkbox.stateChanged.connect(self.checkbox_changed)

    def checkbox_changed(self, state):
        # state arrives as an int: 0 for unchecked, 2 for checked
        # (1 would be PartiallyChecked, only relevant if the checkbox is tri-state).
        # Comparing against Qt.Checked instead of a raw 2 keeps the intent clear.
        if state == Qt.Checked:
            print("You like food")
        else:
            print("You DO NOT like food")


if __name__ == '__main__':
    app = QApplication(sys.argv)  # one QApplication per app, handles the event system
    window = MainWindow()
    window.show()  # widgets are invisible by default until you call show()
    sys.exit(app.exec_())  # exec_() starts the event loop, this line blocks until the app closes