"""Creates the base guiTab window for the guiWindow class."""

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from swearjar.GUI.fieldLineEdit import fieldLineEdit
from functools import partial


class GUITab(QWidget):
    """Creates a GUITab for the GUIWindow."""

    def __init__(self, initParams):
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
        self.leftColumn.setAlignment(Qt.AlignRight)
        self.rightColumn = QVBoxLayout()

        self.picture = QLabel()
        # pixmap = QPixmap('coolit/GUI/img/CoolingTowerWet-Default.png')
        # self.picture.setPixmap(pixmap)

        self.initParams = initParams

    def makeLayout(self, heading):
        """
        Make the layout for window and set it.

        Layouts
        -------
        * leftColumn: Refers to the column next to the image.
                      Contains the labelFieldLayout.
        * rightColumn: Refers to the column containing the image.
        * labelFieldLayout: Contains the label and field to be filled
                            in by the user. It is composed of two column's,
                            one for the label, and another for the field.
        * mainLayout: Contains all sub layouts (leftColumn, labelFieldLayout)
                      and widgets for the tab.
        """
        params = self.initParams.getParamsFromHeading(heading)
        for param in params:
            self.addRow(param, self.initParams[param])

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

        self.setLayout(self.mainLayout)

    def addRow(self, param, val):
        """Add a row to the widget."""
        labelWidget = QLabel(self.initParams.getlabel(param))
        labelWidget.setAlignment(Qt.AlignRight | Qt.AlignVCenter)

        fieldWidget = fieldLineEdit(name=param)
        fieldWidget.setValue(val)
        fieldWidget.changePic.connect(partial(self.changePic,
                                              fieldWidget.name))

        self.paramToWidget[param] = fieldWidget

        self.labelVbox.addWidget(labelWidget)
        self.fieldVbox.addWidget(fieldWidget)

    def getInput(self):
        """Take the values from the input fields."""
        for param, widget in self.paramToWidget.items():
            self.initParams[param] = widget.value()
        return self.initParams

    def updateInput(self, updateDict):
        """Update the fields to display values according to a dictionary."""
        for param, widget in self.paramToWidget.items():
            val = updateDict[param]
            widget.setValue(val)

    def changePic(self, name):
        """Change the picture on the tab."""
        # pixmap = QPixmap('coolit/GUI/img/CoolingTowerWet-Default.png')
        # self.picture.setPixmap(pixmap)
        pass


if __name__ == '__main__':
    pass
