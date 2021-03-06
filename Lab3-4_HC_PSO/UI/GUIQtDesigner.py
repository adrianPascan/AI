# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUIQtDesigner.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.resultLabel = QtWidgets.QLabel(self.centralwidget)
        self.resultLabel.setObjectName("resultLabel")
        self.verticalLayout.addWidget(self.resultLabel)
        self.resultTextEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.resultTextEdit.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.resultTextEdit.setObjectName("resultTextEdit")
        self.verticalLayout.addWidget(self.resultTextEdit)
        self.horizontalLayout.addLayout(self.verticalLayout)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.probabilityOfMutationAndCrossoverLabel = QtWidgets.QLabel(self.centralwidget)
        self.probabilityOfMutationAndCrossoverLabel.setObjectName("probabilityOfMutationAndCrossoverLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.probabilityOfMutationAndCrossoverLabel)
        self.probabilityOfMutationAndCrossoverLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.probabilityOfMutationAndCrossoverLineEdit.setObjectName("probabilityOfMutationAndCrossoverLineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.probabilityOfMutationAndCrossoverLineEdit)
        self.populationSizeLabel = QtWidgets.QLabel(self.centralwidget)
        self.populationSizeLabel.setObjectName("populationSizeLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.populationSizeLabel)
        self.populationSizeLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.populationSizeLineEdit.setObjectName("populationSizeLineEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.populationSizeLineEdit)
        self.noOfIterationsLabel = QtWidgets.QLabel(self.centralwidget)
        self.noOfIterationsLabel.setObjectName("noOfIterationsLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.noOfIterationsLabel)
        self.noOfIterationsLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.noOfIterationsLineEdit.setObjectName("noOfIterationsLineEdit")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.noOfIterationsLineEdit)
        self.verticalLayout_2.addLayout(self.formLayout)
        self.runPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.runPushButton.setObjectName("runPushButton")
        self.verticalLayout_2.addWidget(self.runPushButton)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_2.addItem(spacerItem1)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_2.addWidget(self.line)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_2.addItem(spacerItem2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setObjectName("formLayout_2")
        self.noOfParticlesLabel = QtWidgets.QLabel(self.centralwidget)
        self.noOfParticlesLabel.setObjectName("noOfParticlesLabel")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.noOfParticlesLabel)
        self.noOfParticlesLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.noOfParticlesLineEdit.setObjectName("noOfParticlesLineEdit")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.noOfParticlesLineEdit)
        self.sizeOfParticleLabel = QtWidgets.QLabel(self.centralwidget)
        self.sizeOfParticleLabel.setObjectName("sizeOfParticleLabel")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.sizeOfParticleLabel)
        self.sizeOfParticleLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.sizeOfParticleLineEdit.setObjectName("sizeOfParticleLineEdit")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.sizeOfParticleLineEdit)
        self.sizeOfIndividualLabel = QtWidgets.QLabel(self.centralwidget)
        self.sizeOfIndividualLabel.setObjectName("sizeOfIndividualLabel")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.sizeOfIndividualLabel)
        self.sizeOfIndividualLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.sizeOfIndividualLineEdit.setObjectName("sizeOfIndividualLineEdit")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.sizeOfIndividualLineEdit)
        self.noOfNeighboursLabel = QtWidgets.QLabel(self.centralwidget)
        self.noOfNeighboursLabel.setObjectName("noOfNeighboursLabel")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.noOfNeighboursLabel)
        self.noOfNeighboursLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.noOfNeighboursLineEdit.setObjectName("noOfNeighboursLineEdit")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.noOfNeighboursLineEdit)
        self.noOfIterationsPSOLabel = QtWidgets.QLabel(self.centralwidget)
        self.noOfIterationsPSOLabel.setObjectName("noOfIterationsPSOLabel")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.noOfIterationsPSOLabel)
        self.noOfIterationsPSOLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.noOfIterationsPSOLineEdit.setObjectName("noOfIterationsPSOLineEdit")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.noOfIterationsPSOLineEdit)
        self.verticalLayout_3.addLayout(self.formLayout_2)
        self.runPSOPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.runPSOPushButton.setObjectName("runPSOPushButton")
        self.verticalLayout_3.addWidget(self.runPSOPushButton)
        self.verticalLayout_2.addLayout(self.verticalLayout_3)
        self.verticalLayout_4.addLayout(self.verticalLayout_2)
        self.horizontalLayout.addLayout(self.verticalLayout_4)
        self.verticalLayout_5.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.resultLabel.setText(_translate("MainWindow", "RESULT: "))
        self.probabilityOfMutationAndCrossoverLabel.setText(_translate("MainWindow", "Probability of Mutation and Crossover: "))
        self.populationSizeLabel.setText(_translate("MainWindow", "Population size: "))
        self.noOfIterationsLabel.setText(_translate("MainWindow", "No. of Iterations"))
        self.runPushButton.setText(_translate("MainWindow", "RUN EA+HC"))
        self.noOfParticlesLabel.setText(_translate("MainWindow", "No. of Particles: "))
        self.sizeOfParticleLabel.setText(_translate("MainWindow", "Size of Particle: "))
        self.sizeOfIndividualLabel.setText(_translate("MainWindow", "Size of Individual: "))
        self.noOfNeighboursLabel.setText(_translate("MainWindow", "No. of Neighbours: "))
        self.noOfIterationsPSOLabel.setText(_translate("MainWindow", "No. of Iterations"))
        self.runPSOPushButton.setText(_translate("MainWindow", "RUN PSO"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
