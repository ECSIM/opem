from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from opem.Amphlett_Params import *



class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.main = QVBoxLayout(self)
        self.attributes = {}
        self.name = QLabel('OPEM')
        self.name.setAlignment(Qt.AlignCenter)
        self.main.addWidget(self.name)
        for f in self.get_attr_fields():
            self.main.addLayout(f)

        self.reset = QPushButton('Reset')
        self.analyse = QPushButton('Analyse')
        self.main.addLayout(self.get_buttons())
        self.setLayout(self.main)

    def get_attr_fields(self):
        fields = []
        for item in list(InputParams.keys()):
            field = QHBoxLayout(self)
            label = QLabel(item + ' ( ' + InputParams[item] + ' ) : ')
            field.addWidget(label)
            self.attributes[item] = QDoubleSpinBox(self)
            self.attributes[item].setRange(0, 1000)
            self.attributes[item].setMaximumSize(200, 20)
            self.attributes[item].setMinimumSize(100, 20)
            field.addWidget(self.attributes[item])
            fields.append(field)
        return fields

    def get_buttons(self):
        layout = QHBoxLayout(self)
        layout.addWidget(self.reset)
        layout.addWidget(self.analyse)
        self.reset.clicked.connect(self.reset_slt)
        self.analyse.clicked.connect(self.analyse_slt)
        return layout

    def reset_slt(self):
        for k in self.attributes.keys():
            self.attributes[k].setValue(0.0)
        print('reset')

    def analyse_slt(self):
        print('analyse')
