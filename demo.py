import pickle
import pandas as pd
model = None

with open("model.pkl", "rb") as file:
    model = pickle.load(file)



data = pd.DataFrame(data=[[84,23,73,0,7,3]], columns=["Attendance", "Hours_Studied", "Previous_Scores", "Tutoring_Sessions", "Sleep_Hours", "Physical_Activity"])

print(model.predict(data))

from PySide6 import QtCore, QtWidgets, QtGui
import sys

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.button = QtWidgets.QPushButton("Predict")
        self.text = QtWidgets.QLabel("", alignment=QtCore.Qt.AlignCenter)


        self.layout = QtWidgets.QVBoxLayout(self)
        horizontalLayout = QtWidgets.QHBoxLayout(self)
        verticalLayout = QtWidgets.QVBoxLayout()
        self.numberboxes = []
        for column in ["Percentage of classes attended", "Hours studied per week", "Score from previous exam", "Tutoring sessions attended per month", "Hours of sleep per night", "Hours spent on physical activity per week"]:
            pair = QtWidgets.QHBoxLayout()
            widget = QtWidgets.QSpinBox()
            label = QtWidgets.QLabel(column)

            pair.addWidget(label)
            pair.addWidget(widget)
            self.numberboxes.append(widget)
            verticalLayout.addLayout(pair)
        horizontalLayout.addLayout(verticalLayout)
        self.layout.addLayout(horizontalLayout)
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.button)

        self.button.clicked.connect(self.calculate)

    @QtCore.Slot()
    def calculate(self):
        data = [int(el.value()) for el in self.numberboxes]
        input = pd.DataFrame(data=[data], columns=["Attendance", "Hours_Studied", "Previous_Scores", "Tutoring_Sessions", "Sleep_Hours", "Physical_Activity"])
        prediction = model.predict(input)[0]
        self.text.setText(str(round(prediction,1)))

if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = MyWidget()
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec())


