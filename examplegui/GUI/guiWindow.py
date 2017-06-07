# ---------------------------------------------------------------------------
#
#  ExampleGUI: An example GUI for the ESDLab.
#
#  Copyright (C) 2017 by Energy Systems Design Laboratory, University of Alberta
#
#  This software is distributed under the MIT License.
#  For more information, see LICENSE.txt file
#
#  - Class: GUIWindow
#  - Description: Creates the GUI window.
#  - Developers: J. Cook
#
# ---------------------------------------------------------------------------
"""Creates the main GUI window."""

from PyQt5.QtWidgets import (QMainWindow, QHBoxLayout, QVBoxLayout,
                             QMessageBox, QWidget, QPushButton, QFileDialog,
                             QAction)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from examplegui.GUI.CreateTabs import CreateTabs
from examplegui.InputOutput import fileInput, fileOutput
from examplegui.myEquations import myEquations


class GUIWindow(QMainWindow):
    """Creates the ExampleGUI GUIWindow."""

    def __init__(self, initParams):
        """Initialize the window class, then its super class."""
        super().__init__()

        self.initParams = initParams
        self.initUI()

    def initUI(self):
        """Initialize the window and its processes."""
        self.centralWidget = self.createCentralWidget()
        self.setCentralWidget(self.centralWidget)

        self.createMenuBar()

        self.showMaximized()
        self.setWindowTitle('ExampleGUI')
        self.setWindowIcon(QIcon('examplegui/GUI/img/ESDL_logo.jpg'))
        self.show()

    def createCentralWidget(self):
        """Create the central widget for the MainWindow.

        Returns:
            A QWidget to be used as the central widget in the main window.

        """
        btnQuit = QPushButton("Quit", self)
        btnQuit.setObjectName("Quit Button")
        btnQuit.clicked.connect(self.close)

        btnRun = QPushButton("Run", self)
        btnRun.setObjectName("Run Button")
        btnRun.clicked.connect(self.runSimulation)

        tabs = CreateTabs(self.initParams)
        tabs.setObjectName("Tabs Widget")
        centralWidget = QWidget()

        hbox_RunQuitButtons = QHBoxLayout()
        hbox_RunQuitButtons.addStretch(1)
        hbox_RunQuitButtons.addWidget(btnRun)
        hbox_RunQuitButtons.addWidget(btnQuit)

        vbox = QVBoxLayout()
        vbox.addWidget(tabs)
        vbox.addLayout(hbox_RunQuitButtons)

        centralWidget.setLayout(vbox)

        return centralWidget

    def createMenuBar(self):
        """Create the menu bar for the Main Window."""
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')

        loadAction = QAction("Load", self)
        loadAction.setShortcut("Ctrl+L")
        loadAction.triggered.connect(self.loadFromFile)

        runSimulationAction = QAction("Run Simulation", self)
        runSimulationAction.setShortcut("Ctrl+R")
        runSimulationAction.triggered.connect(self.runSimulation)

        fileMenu.addAction(loadAction)
        fileMenu.addAction(runSimulationAction)

    def loadFromFile(self):
        """Load the initial parameters from a text file."""
        inputName = QFileDialog.getOpenFileName(
                                        self,
                                        caption="Get Input Parameters",
                                        directory="output/output.txt",
                                        initialFilter="*.txt",
                                        filter="*.txt")[0]

        # Covers the case where cancel is pressed, rather than save
        if inputName != '':
            self.initParams = fileInput.updateDict(self.initParams, inputName)
            tabs = self.findChild(CreateTabs, "Tabs Widget")
            tabs.updateInput(self.initParams)
            print("Load a File")
        else:
            cancelBox = QMessageBox()
            cancelBox.setText("No input has been chosen.")
            cancelBox.exec()

    def keyPressEvent(self, event):
        """Close application from escape key."""
        if event.key() == Qt.Key_Escape:
            self.close()

    def closeEvent(self, event):
        """Generate 'question' dialog on closing window."""
        reply = QMessageBox.question(
            self, "Message",
            "Are you sure you want to quit? Any unsaved work will be lost.",
            QMessageBox.Close | QMessageBox.Cancel,
            QMessageBox.Cancel)

        if reply == QMessageBox.Close:
            event.accept()
        else:
            event.ignore()

    def runSimulation(self):
        """Run Cooling tower simulation with current parameters."""
        tabs = self.findChild(CreateTabs, "Tabs Widget")
        paramsDict = tabs.getInput()

        # Check to see if there are any missing parameters
        missingParams = []
        for key, val in paramsDict.items():
            if val is None:
                missingParams.append(key)

        if not missingParams:
            outputName = QFileDialog.getSaveFileName(
                                        self,
                                        caption="Save Simulation Results As",
                                        directory="output/output.txt",
                                        initialFilter="*.txt",
                                        filter="*.txt")[0]

            # Covers the case where cancel is pressed, rather than save
            if outputName != '':
                # There should be an official way to add .txt at end of file
                if outputName[-4:] != ".txt":
                    outputName += ".txt"

                # Run the Simulation
                myEq = myEquations(paramsDict)
                results = myEq.solve()

                fileOutput.writeReport(paramsDict,
                                       results,
                                       outputName)

                resultsBox = QMessageBox()
                resultsBox.setText("Results have been saved to " + outputName)
                resultsBox.exec()
            else:
                cancelBox = QMessageBox()
                cancelBox.setText("Results have been cancelled.")
                cancelBox.exec()
        else:
            messageStr = ""
            for param in missingParams:
                if messageStr == "":
                    messageStr += param
                else:
                    messageStr = messageStr + ", " + param
            missingParamsBox = QMessageBox()
            missingParamsBox.setText("You are missing the following "
                                     + "parameters and/or they are "
                                     + "too large/small:\n"
                                     + "\n" + messageStr + "\n\n"
                                     + "Please enter in an appropriate value "
                                     + "for them and try again.")
            missingParamsBox.exec()


if __name__ == '__main__':
    pass
