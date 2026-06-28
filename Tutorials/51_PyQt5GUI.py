import sys
# QApplication = manages the GUI app itself, every PyQt app needs exactly one
# QMainWindow = a ready made window template with title bar, resize, close button etc
from PyQt5.QtWidgets import QApplication, QMainWindow

# QIcon lets you set a custom icon image for the window
from PyQt5.QtGui import QIcon


# inherits from QMainWindow, so it gets all default window behavior for free
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()  # runs QMainWindow's own setup code first

        self.setWindowTitle("My cool first GUI")  # text shown in the title bar

        # setGeometry(x, y, width, height)
        # x, y = position of top left corner on screen
        # width, height = size of the window in pixels
        self.setGeometry(700, 300, 500, 500)

        self.setWindowIcon(QIcon("C:\\Users\\T4WSIF\\Desktop\\PyNotes\\Tutorials\\profile_pic.jpg")) # sets the window icon to a custom image, make sure the path is correct


def main():
    # every PyQt app needs one QApplication instance
    # sys.argv passes command line arguments into the app, optional but standard practice
    app = QApplication(sys.argv)

    # creates the window object, this runs __init__ above
    window = MainWindow()

    # without this line, the window exists in memory but never appears on screen
    window.show()

    # starts the event loop, keeps the app running and listening for clicks, key presses etc
    # sys.exit() makes sure the app closes with the correct exit code once the loop ends
    sys.exit(app.exec_())


# ensures main() only runs when this file is executed directly
# if this file gets imported elsewhere, main() wont run automatically
if __name__ == "__main__":
    main()