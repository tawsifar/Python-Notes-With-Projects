import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # setGeometry(x, y, width, height)
        # x, y = where the window appears on screen
        # width, height = size of the window
        self.setGeometry(700, 300, 500, 500)

        # basic label with custom font and style
        label = QLabel("Hello", self)  # self = this label belongs to MainWindow
        label.setFont(QFont("Arial", 40))
        label.setGeometry(0, 0, 500, 100)  # position and size INSIDE the window

        # setStyleSheet works like CSS
        label.setStyleSheet(
            "color: #292929;"
            "background-color: #6fdcf7;"
            "font-weight: bold;"
            "font-style: italic;"
            "text-decoration: underline;"
        )

        # IMPORTANT: calling setAlignment() multiple times on the SAME label
        # only the LAST call actually takes effect, earlier ones get overwritten
        # so below, separate labels are used to demonstrate each alignment clearly

        # vertical alignment options
        top_label = QLabel("Top", self)
        top_label.setGeometry(0, 110, 160, 60)
        top_label.setStyleSheet("background-color: lightgray;")
        top_label.setAlignment(Qt.AlignTop)  # text sticks to the top of the label box

        bottom_label = QLabel("Bottom", self)
        bottom_label.setGeometry(170, 110, 160, 60)
        bottom_label.setStyleSheet("background-color: lightgray;")
        bottom_label.setAlignment(Qt.AlignBottom)  # text sticks to the bottom

        vcenter_label = QLabel("VCenter", self)
        vcenter_label.setGeometry(340, 110, 160, 60)
        vcenter_label.setStyleSheet("background-color: lightgray;")
        vcenter_label.setAlignment(Qt.AlignVCenter)  # text centered vertically

        # horizontal alignment options
        left_label = QLabel("Left", self)
        left_label.setGeometry(0, 180, 160, 60)
        left_label.setStyleSheet("background-color: lightyellow;")
        left_label.setAlignment(Qt.AlignLeft)  # text aligned to the left

        right_label = QLabel("Right", self)
        right_label.setGeometry(170, 180, 160, 60)
        right_label.setStyleSheet("background-color: lightyellow;")
        right_label.setAlignment(Qt.AlignRight)  # text aligned to the right

        hcenter_label = QLabel("HCenter", self)
        hcenter_label.setGeometry(340, 180, 160, 60)
        hcenter_label.setStyleSheet("background-color: lightyellow;")
        hcenter_label.setAlignment(Qt.AlignHCenter)  # text centered horizontally

        # combining alignments with the | (pipe) operator
        # pipe lets you mix one vertical + one horizontal rule together
        center_top_label = QLabel("Center+Top", self)
        center_top_label.setGeometry(0, 250, 160, 60)
        center_top_label.setStyleSheet("background-color: lightgreen;")
        center_top_label.setAlignment(Qt.AlignHCenter | Qt.AlignTop)  # centered horizontally, stuck to top

        center_bottom_label = QLabel("Center+Bottom", self)
        center_bottom_label.setGeometry(170, 250, 160, 60)
        center_bottom_label.setStyleSheet("background-color: lightgreen;")
        center_bottom_label.setAlignment(Qt.AlignHCenter | Qt.AlignBottom)  # centered horizontally, stuck to bottom

        full_center_label = QLabel("Full Center", self)
        full_center_label.setGeometry(340, 250, 160, 60)
        full_center_label.setStyleSheet("background-color: lightgreen;")
        full_center_label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        # same result as below, just written manually instead of using the shortcut
        # full_center_label.setAlignment(Qt.AlignCenter)

        # Qt.AlignCenter is a shortcut that means center both horizontally and vertically
        shortcut_label = QLabel("AlignCenter shortcut", self)
        shortcut_label.setGeometry(0, 320, 500, 60)
        shortcut_label.setStyleSheet("background-color: lightpink;")
        shortcut_label.setAlignment(Qt.AlignCenter)


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()