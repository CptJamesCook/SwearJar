"""Contains the Drift Eliminator constants tab."""
from examplegui.GUI.Tabs.guiTab import GUITab


class tabEx2(GUITab):
    """The tab Drift Eliminator Constants."""

    def __init__(self, initParams):
        """Initialize self and parent."""
        paramsTuple = ('Bloot', 'Blort', 'Zarg')
        super().__init__(initParams, paramsTuple)
        self.makeLayout(initParams)
