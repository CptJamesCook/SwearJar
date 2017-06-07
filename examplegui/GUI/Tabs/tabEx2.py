# ---------------------------------------------------------------------------
#
#  ExampleGUI: An example GUI for the ESDLab.
#
#  Copyright (C) 2017 by Energy Systems Design Laboratory, University of Alberta
#
#  This software is distributed under the MIT License.
#  For more information, see LICENSE.txt file
#
#  - Class: tabEx2
#  - Description: Contains the Example 2 tab.
#  - Developers: J. Cook
#
# ---------------------------------------------------------------------------
"""Contains the Drift Eliminator constants tab."""
from examplegui.GUI.Tabs.guiTab import GUITab


class tabEx2(GUITab):
    """The tab Drift Eliminator Constants."""

    def __init__(self, initParams):
        """Initialize self and parent."""
        paramsTuple = ('Bloot', 'Blort', 'Zarg')
        super().__init__(initParams, paramsTuple)
        self.makeLayout(initParams)
