import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import QTimer, QTime, Qt
from PyQt5.QtGui import QFont, QFontDatabase


class DigitalClock(QWidget):
    def __init__(self):
        super().__init__()

        # QLabel will display the time text
        self.time_label = QLabel(self)

        # QTimer fires a signal repeatedly at a set interval
        # used here to update the clock every second
        self.timer = QTimer(self)

        self.initUI()

    def initUI(self):
        self.setWindowTitle("Digital Clock")
        self.setGeometry(600, 400, 300, 100)  # x, y, width, height

        # VBoxLayout stacks the label vertically inside the window
        vbox = QVBoxLayout()
        vbox.addWidget(self.time_label)
        self.setLayout(vbox)

        self.time_label.setAlignment(Qt.AlignCenter)  # center the time text inside the label

        # hsl(111, 100%, 50%) is a bright green color
        # font-size 150px makes the digits fill the window
        self.time_label.setStyleSheet("font-size: 150px;"
                                       "color: hsl(111, 100%, 50%);")

        # black background applied to the whole window widget
        self.setStyleSheet("background-color: black;")

        # optional custom font block — uncomment to use a digital style font file
        # QFontDatabase.addApplicationFont() loads a .TTF font file from disk
        # applicationFontFamilies() returns the font family name from that file
        # then QFont() creates a font object using that family at size 150
        # font_id = QFontDatabase.addApplicationFont("DS-DIGIT.TTF")
        # font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
        # my_font = QFont(font_family, 150)
        # self.time_label.setFont(my_font)

        # connect the timer's timeout signal to update_time
        # every time the timer fires, update_time() is called automatically
        self.timer.timeout.connect(self.update_time)

        # start the timer, fires every 1000 milliseconds = every 1 second
        self.timer.start(1000)

        # call once immediately so the clock shows time on launch
        # without this there would be a 1 second blank gap before the first tick
        self.update_time()

    def update_time(self):
        # QTime.currentTime() gets the current system time
        # toString("hh:mm:ss AP") formats it as 12 hour time with AM/PM
        # for 24 hour format use "hh:mm:ss" without AP
        current_time = QTime.currentTime().toString("hh:mm:ss AP")

        # update the label text with the new time string every second
        self.time_label.setText(current_time)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    clock = DigitalClock()
    clock.show()
    sys.exit(app.exec_())