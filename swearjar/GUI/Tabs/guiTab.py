"""Creates the base guiTab window for the guiWindow class."""

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from examplegui.GUI.fieldLineEdit import fieldLineEdit
from examplegui.InputOutput.ParamToLabel import paramToLabel
from functools import partial


class GUITab(QWidget):
    """Creates a GUITab for the GUIWindow."""

    def __init__(self, initDict, paramsTuple):
        """Initialize the itself, then its super class."""
        super().__init__()

        # Associate each param with a widget
        self.paramToWidget = {}

        self.fieldVbox = QVBoxLayout()
        self.labelVbox = QVBoxLayout()
        self.labelFieldLayout = QHBoxLayout()
        self.labelFieldLayout.addLayout(self.labelVbox)
        self.labelFieldLayout.addLayout(self.fieldVbox)

        self.mainLayout = QHBoxLayout()
        self.leftColumn = QVBoxLayout()
        self.rightColumn = QVBoxLayout()

        self.picture = QLabel()
        pixmap = QPixmap('examplegui/GUI/img/ESDL_logo.jpg')
        self.picture.setPixmap(pixmap)

        self.params = paramsTuple

    def makeLayout(self, initDict):
        """
        Make the layout for window and set it.

        Layouts
        -------
        * leftColumn: Refers to the column next to the image.
                      Contains the labelFieldLayout.
        * labelFieldLayout: Contains the label and field to be filled
                            in by the user.
        * mainLayout: Contains all sub layouts (leftColumn, labelFieldLayout)
                      and widgets for the tab.
        """
        for param in self.params:
            self.addRow(param, initDict[param])

        self.leftColumn.addStretch(1)
        self.leftColumn.addLayout(self.labelFieldLayout)
        self.leftColumn.addStretch(1)

        self.rightColumn.addStretch(1)
        self.rightColumn.addWidget(self.picture)
        self.rightColumn.addStretch(1)

        self.mainLayout.addStretch(1)
        self.mainLayout.addLayout(self.leftColumn)
        self.mainLayout.addStretch(1)
        self.mainLayout.addLayout(self.rightColumn)
        self.mainLayout.addStretch(1)

        self.setLayout(self.mainLayout)

    def addRow(self, param, val):
        """Add a row to the widget."""
        labelWidget = QLabel(paramToLabel[param])
        labelWidget.setAlignment(Qt.AlignRight | Qt.AlignVCenter)

        fieldWidget = fieldLineEdit()
        fieldWidget.setValue(str(val))
        fieldWidget.changePic.connect(partial(self.changePic,
                                              fieldWidget.name))

        self.paramToWidget[param] = fieldWidget

        self.labelVbox.addWidget(labelWidget)
        self.fieldVbox.addWidget(fieldWidget)

    def getInput(self):
        """Take the values from the input fields."""
        returnDict = {}
        for param, widget in self.paramToWidget.items():
            returnDict[param] = widget.value()

        return returnDict

    def updateInput(self, updateDict):
        """Update the fields to display values according to a dictionary."""
        for param, widget in self.paramToWidget.items():
            val = updateDict[param]
            widget.setText(str(val))

    def changePic(self, name):
        """Change the picture on the tab."""
        pixmap = QPixmap('examplegui/GUI/img/ESDL_logo.jpg')
        self.picture.setPixmap(pixmap)


if __name__ == '__main__':
    pass
