import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel,
                              QPushButton, QVBoxLayout, QHBoxLayout)
from PyQt5.QtCore import QTimer, QTime, Qt


class Stopwatch(QWidget):
    def __init__(self):
        super().__init__()

        # QTime(hour, minute, second, millisecond) — starts at zero
        self.time = QTime(0, 0, 0, 0)

        self.time_label = QLabel("00:00:00.00", self)
        self.start_button = QPushButton("Start", self)
        self.stop_button = QPushButton("Stop", self)
        self.reset_button = QPushButton("Reset", self)

        # QTimer will fire every 10ms to update the display
        self.timer = QTimer(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Stopwatch")

        # vbox is the main vertical layout — holds the time label on top
        # and the hbox (button row) below it
        vbox = QVBoxLayout()
        vbox.addWidget(self.time_label)
        self.setLayout(vbox)

        self.time_label.setAlignment(Qt.AlignCenter)

        # hbox holds the three buttons side by side in one row
        hbox = QHBoxLayout()
        hbox.addWidget(self.start_button)
        hbox.addWidget(self.stop_button)
        hbox.addWidget(self.reset_button)

        # nest the hbox inside the vbox so buttons sit below the label
        vbox.addLayout(hbox)

        # stylesheet targets specific widget types using QPushButton and QLabel selectors
        # shared styles go in the combined block, unique styles go in separate blocks
        self.setStyleSheet("""
            QPushButton, QLabel {
                padding: 20px;
                font-weight: bold;
                font-family: calibri;
            }
            QPushButton {
                font-size: 50px;
            }
            QLabel {
                font-size: 120px;
                background-color: hsl(200, 100%, 85%);
                border-radius: 20px;
            }
        """)

        # connect each button's clicked signal to its matching slot method
        self.start_button.clicked.connect(self.start)
        self.stop_button.clicked.connect(self.stop)
        self.reset_button.clicked.connect(self.reset)

        # every time the timer fires (every 10ms), update_display() runs
        self.timer.timeout.connect(self.update_display)

    def start(self):
        # start(10) means the timer fires every 10 milliseconds
        self.timer.start(10)

    def stop(self):
        # stop() pauses the timer without resetting the time
        self.timer.stop()

    def reset(self):
        self.timer.stop()
        self.time = QTime(0, 0, 0, 0)  # reset time back to zero
        self.time_label.setText(self.format_time(self.time))  # update display immediately

    def format_time(self, time):
        hours = time.hour()
        minutes = time.minute()
        seconds = time.second()

        # msec() returns full milliseconds (0-999)
        # // 10 converts it to centiseconds (0-99) for a 2 digit display
        milliseconds = time.msec() // 10

        # :02 ensures each value is always 2 digits, e.g. 5 becomes 05
        return f"{hours:02}:{minutes:02}:{seconds:02}.{milliseconds:02}"

    def update_display(self):
        # addMSecs(10) adds 10 milliseconds to the current time each tick
        # QTime is immutable so it returns a new QTime object instead of modifying in place
        self.time = self.time.addMSecs(10)
        self.time_label.setText(self.format_time(self.time))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    stopwatch = Stopwatch()
    stopwatch.show()
    sys.exit(app.exec_())