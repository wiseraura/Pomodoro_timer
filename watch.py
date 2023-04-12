from PyQt5.QtCore import QTimer, QTime, Qt
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QVBoxLayout, QWidget, QPushButton

class Pomodoro(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Pomodoro Timer")
        self.setGeometry(100, 100, 400, 400)

        # create the timer label, start button, and reset button
        self.timer_label = QLabel("25:00")
        self.timer_label.setObjectName("timerLabel")
        self.timer_label.setAlignment(Qt.AlignCenter)
        self.start_button = QPushButton("Start")
        self.reset_button = QPushButton("Reset")
        self.start_button.clicked.connect(self.start_timer)
        self.reset_button.clicked.connect(self.reset_timer)

        # create a vertical layout and add the label and buttons to it
        layout = QVBoxLayout()

        # add the watch label and timer label to the layout
        layout.addWidget(self.timer_label)
        layout.addWidget(self.start_button)
        layout.addWidget(self.reset_button)

        # create a widget to hold the layout
        widget = QWidget()
        widget.setLayout(layout)

        # set the widget as the central widget of the window
        self.setCentralWidget(widget)

        # create the timer and set its interval to 1 second
        self.timer = QTimer()
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.update_timer)

        # set the initial time
        self.time_remaining = QTime(0, 25, 0)

        # set the initial state to "work"
        self.state = "work"

    def start_timer(self):
        self.timer.start()

    def reset_timer(self):
        self.timer.stop()
        self.time_remaining = QTime(0, 25, 0)
        self.timer_label.setText(self.time_remaining.toString("mm:ss"))
        self.start_button.setEnabled(True)

        # set the initial state to "work"
        self.state = "work"

    def update_timer(self):
        # decrement the time remaining by 1 second
        self.time_remaining = self.time_remaining.addSecs(-1)

        # update the timer label with the new time
        self.timer_label.setText(self.time_remaining.toString("mm:ss"))

        # if the timer has reached 0, stop the timer and show a message
        if self.time_remaining == QTime(0, 0, 0):
            self.timer.stop()

            if self.state == "work":
                # start a break timer
                self.time_remaining = QTime(0, 5, 0)
                self.timer_label.setText("Break")
                self.state = "break"
            else:
                # start a work timer
                self.time_remaining = QTime(0, 25, 0)
                self.timer_label.setText("25:00")
                self.state = "work"

            self.start_button.setEnabled(False)
            self.timer.start()

    def start_break(self):
        self.breakTimer.stop()
        self.time_remaining = QTime(0, 5, 0)
        self.timer_label.setText(self.time_remaining.toString("mm:ss"))
        self.timer.start(1000)

if __name__ == '__main__':
    app = QApplication([])
    pomodoro = Pomodoro()
    pomodoro.setStyleSheet("#timerLabel { \
                                border-radius: 50px; \
                                border: 2px solid black; \
                                padding: 60px; \
                                background-color: blue; \
                                font-size: 75px; \
                           }")
    pomodoro.show()
    app.exec()
