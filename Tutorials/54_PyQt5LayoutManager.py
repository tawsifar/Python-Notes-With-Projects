import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel,
                              QWidget, QVBoxLayout, QHBoxLayout, QGridLayout)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700, 300, 500, 500)
        self.initUI()

    def initUI(self):
        # QMainWindow cant have a layout set directly
        # so a blank QWidget is used as the container that holds the layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        label1 = QLabel("#1")
        label2 = QLabel("#2")
        label3 = QLabel("#3")
        label4 = QLabel("#4")
        label5 = QLabel("#5")

        label1.setStyleSheet("background-color: red;")
        label2.setStyleSheet("background-color: yellow;")
        label3.setStyleSheet("background-color: green;")
        label4.setStyleSheet("background-color: blue;")
        label5.setStyleSheet("background-color: purple;")

        # VBOX — stacks widgets top to bottom
        # result:
        # [1]
        # [2]
        # [3]
        # [4]
        # [5]
        # vbox = QVBoxLayout()
        # vbox.addWidget(label1)
        # vbox.addWidget(label2)
        # vbox.addWidget(label3)
        # vbox.addWidget(label4)
        # vbox.addWidget(label5)
        # central_widget.setLayout(vbox)

        # HBOX — places widgets left to right
        # result:
        # [1][2][3][4][5]
        # hbox = QHBoxLayout()
        # hbox.addWidget(label1)
        # hbox.addWidget(label2)
        # hbox.addWidget(label3)
        # hbox.addWidget(label4)
        # hbox.addWidget(label5)
        # central_widget.setLayout(hbox)

        # GRID — places widgets by row and column
        # addWidget(widget, row, column) — both start from 0
        # result:
        # [1][2]
        # [3][4][5]
        grid = QGridLayout()

        grid.addWidget(label1, 0, 0)  # row 0, col 0
        grid.addWidget(label2, 0, 1)  # row 0, col 1
        grid.addWidget(label3, 1, 0)  # row 1, col 0
        grid.addWidget(label4, 1, 1)  # row 1, col 1
        grid.addWidget(label5, 1, 2)  # row 1, col 2 — third column only in row 1

        central_widget.setLayout(grid)

        # only ONE layout can be active at a time
        # to switch, comment out the current one and uncomment another
        # all three layouts auto resize when the window is resized
        # unlike setGeometry() which uses fixed pixel positions


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()