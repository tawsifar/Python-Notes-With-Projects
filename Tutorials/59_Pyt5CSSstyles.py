# PyQt5 setStyleSheet()
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QHBoxLayout

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # create three buttons
        self.button1 = QPushButton("#1")
        self.button2 = QPushButton("#2")
        self.button3 = QPushButton("#3")
        self.initUI()

    def initUI(self):
        # QMainWindow does not support layouts directly
        # so we create a QWidget and set it as the central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # QHBoxLayout arranges widgets horizontally side by side
        hbox = QHBoxLayout()

        # add all three buttons to the layout
        hbox.addWidget(self.button1)
        hbox.addWidget(self.button2)
        hbox.addWidget(self.button3)

        # apply the layout to central_widget
        central_widget.setLayout(hbox)

        # give each button a unique ID so they can be styled individually in CSS
        self.button1.setObjectName("button1")
        self.button2.setObjectName("button2")
        self.button3.setObjectName("button3")

        self.setStyleSheet("""
            QPushButton{
                font-size: 40px;
                font-family: Arial;
                padding: 15px 75px;   /* 15px top-bottom, 75px left-right inner space */
                margin: 25px;         /* 25px outer space around button */
                border: 3px solid;    /* 3px solid border */
                border-radius: 15px;  /* rounded corners */
            }

            /* select specific button using objectName */
            QPushButton#button1{
                background-color: hsl(0, 100%, 64%);    /* red */
            }
            QPushButton#button2{
                background-color: hsl(122, 100%, 64%);  /* green */
            }
            QPushButton#button3{
                background-color: hsl(204, 100%, 64%);  /* blue */
            }

            /* :hover triggers when mouse is over the button, lightness increases */
            QPushButton#button1:hover{
                background-color: hsl(0, 100%, 84%);    /* light red */
            }
            QPushButton#button2:hover{
                background-color: hsl(122, 100%, 84%);  /* light green */
            }
            QPushButton#button3:hover{
                background-color: hsl(204, 100%, 84%);  /* light blue */
            }
        """)

if __name__ == '__main__':
    # initialize PyQt5 application
    app = QApplication(sys.argv)

    # create MainWindow instance
    window = MainWindow()

    # show the window
    window.show()

    # keep app running, exit when window is closed
    sys.exit(app.exec_())