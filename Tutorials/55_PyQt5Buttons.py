import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700, 300, 500, 500)

        # QPushButton creates a clickable button
        # "Click me!" is the text shown on the button
        # self means it belongs to this window
        self.button = QPushButton("Click me!", self)
        self.initUI()

    def initUI(self):
        # position and size of the button inside the window
        # setGeometry(x, y, width, height)
        self.button.setGeometry(150, 200, 200, 100)

        self.button.setStyleSheet("font-size: 30px;")

        # .clicked is a signal — it fires whenever the button is pressed
        # .connect() links that signal to a function (called a slot)
        # so every time the button is clicked, on_click() runs automatically
        self.button.clicked.connect(self.on_click)

    # this is the slot — the function that runs when the button is clicked
    def on_click(self):
        print("Button clicked!")


# __name__ typo fix: original had _name_ (single underscores), needs double: __name__
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())