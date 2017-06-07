# ---------------------------------------------------------------------------
#
#  ExampleGUI: An example GUI for the ESDLab
#
#  Copyright (C) 2017 by Energy Systems Design Laboratory, University of Alberta
#
#  This software is distributed under the MIT License.
#  For more information, see LICENSE.txt file
#
#  - Class: CreateTabs
#  - Description: Takes in, and creates the tabs for the main window.
#  - Developers: J. Cook
#
# ---------------------------------------------------------------------------
"""Sets the tabs for the MainWindow."""
from PyQt5.QtWidgets import QTabWidget
from examplegui.GUI.Tabs import (tabEx1, tabEx2)


class CreateTabs(QTabWidget):
    """Creates the tabs for the GUIWindow."""

    def __init__(self, initParams):
        """Initialize self, then make and add tabs to self."""
        super().__init__()

        self.initParams = initParams
        self.addTab(tabEx1(initParams), "Tab Ex1")
        self.addTab(tabEx2(initParams), "Tab Ex2")

    def getInput(self):
        """
        Iterate over tabs and update our dictionary to the user input.

        Returns:
            An updated initial parameters dictionary.
        """
        for tabIndex in range(0, self.count()):
            widgetAtIndex = self.widget(tabIndex)
            self.initParams.update(widgetAtIndex.getInput())
        return self.initParams

    def updateInput(self, updateDict):
        """Iterate over tabs and update their parameters with a dictionary."""
        for tabIndex in range(0, self.count()):
            widgetAtIndex = self.widget(tabIndex)
            widgetAtIndex.updateInput(updateDict)


if __name__ == "__main__":
    pass
