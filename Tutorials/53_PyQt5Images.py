import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QPixmap

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700, 300, 500, 500)  # x, y, width, height of the window on screen

        # QLabel acts as the image container here, no text involved
        label = QLabel(self)
        label.setGeometry(0, 0, 500, 500)  # label fills the entire window

        # QPixmap loads the image from a file
        # image must be in the same folder as this script
        # or provide a full path like "C:/Users/HP/Desktop/profile_pic.jpg"
        pixmap = QPixmap("C:\\Users\\T4WSIF\\Desktop\\PyNotes\\Tutorials\\profile_pic.jpg")

        # attach the loaded image to the label
        label.setPixmap(pixmap)

        # stretch the image to fill the full label size
        # without this, image stays at its original resolution and may be clipped
        label.setScaledContents(True)

        # centering formula: (parent size - child size) // 2 = offset from edge
        # when label and window are the same size (500 == 500), offset = 0
        # so label starts at top left corner, which is fine here
        # this formula becomes useful when label is smaller than the window
        label.setGeometry(
            (self.width() - label.width()) // 2,    # horizontal center offset
            (self.height() - label.height()) // 2,  # vertical center offset
            label.width(),                           # keep same width
            label.height()                           # keep same height
        )


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


# __name__ == "__main__" is True only when this file is run directly
# if this file is imported by another script, this block is skipped
# note: the original code had a typo -> _name_ instead of __name__ (needs double underscores)
if __name__ == "__main__":
    main()