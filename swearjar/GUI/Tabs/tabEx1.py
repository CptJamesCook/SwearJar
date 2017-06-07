"""Contains the Drift Eliminator constants tab."""
from examplegui.GUI.Tabs.guiTab import GUITab


class tabEx1(GUITab):
    """The tab Drift Eliminator Constants."""

    def __init__(self, initParams):
        """Initialize self and parent."""
        paramsTuple = ('Sorp', 'Merp', 'Doot', 'banana')
        super().__init__(initParams, paramsTuple)
        self.makeLayout(initParams)
