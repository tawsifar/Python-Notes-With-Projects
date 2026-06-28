# PyQt5 LineEdit
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # set window position x=700, y=300 and size 500x500
        self.setGeometry(700, 300, 500, 500)

        # create a text input box inside MainWindow
        self.line_edit = QLineEdit(self)

        # create a Submit button
        self.button = QPushButton("Submit", self)

        # call UI setup function
        self.initUI()

    def initUI(self):
        # set line_edit position x=10, y=10 and size 200x40
        self.line_edit.setGeometry(10, 10, 200, 40)

        # set button position x=210, y=10 and size 100x40 (beside line_edit)
        self.button.setGeometry(210, 10, 100, 40)

        # apply CSS styling to line_edit
        self.line_edit.setStyleSheet("font-size: 25px;"
                                     "font-family: Arial")

        # apply CSS styling to button
        self.button.setStyleSheet("font-size: 25px;"
                                  "font-family: Arial")

        # set placeholder hint text, disappears when user types
        self.line_edit.setPlaceholderText("Enter your name")

        # connect button click event to submit function
        self.button.clicked.connect(self.submit)

    def submit(self):
        # get the text user typed in line_edit
        text = self.line_edit.text()

        # print to terminal
        print(f"Hello {text}")

if __name__ == '__main__':
    # initialize PyQt5 application
    app = QApplication(sys.argv)

    # create MainWindow instance
    window = MainWindow()

    # show the window
    window.show()

    # keep app running, exit when window is closed
    sys.exit(app.exec_())