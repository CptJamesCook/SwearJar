"""Contains the Drift Eliminator constants tab."""
from swearjar.GUI.Tabs.guiTab import GUITab


class tabEx1(GUITab):
    """The tab Drift Eliminator Constants."""

    def __init__(self, initParams):
        """Initialize self and parent."""
        super().__init__(initParams)
        heading = 'Example Tab 1'
        self.makeLayout(heading)
