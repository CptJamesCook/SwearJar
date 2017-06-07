# ---------------------------------------------------------------------------
#
#  ExampleGUI: An example GUI for the ESDLab.
#
#  Copyright (C) 2017 by Energy Systems Design Laboratory, University of Alberta
#
#  This software is distributed under the MIT License.
#  For more information, see LICENSE.txt file
#
#  - Class: tabEx1
#  - Description: Contains the Example 1 tab.
#  - Developers: J. Cook
#
# ---------------------------------------------------------------------------
"""Contains the Drift Eliminator constants tab."""
from examplegui.GUI.Tabs.guiTab import GUITab


class tabEx1(GUITab):
    """The tab Drift Eliminator Constants."""

    def __init__(self, initParams):
        """Initialize self and parent."""
        paramsTuple = ('Sorp', 'Merp', 'Doot', 'banana')
        super().__init__(initParams, paramsTuple)
        self.makeLayout(initParams)
