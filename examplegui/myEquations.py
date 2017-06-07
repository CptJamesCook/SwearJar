# ---------------------------------------------------------------------------
#
#  ExampleGUI: An example GUI for the ESDLab
#
#  Copyright (C) 2017 by Energy Systems Design Laboratory, University of Alberta
#
#  This software is distributed under the MIT License.
#  For more information, see LICENSE.txt file
#
#  - Class: MyEquations
#  - Description: This is where my equations/things go.
#  - Developers: J. Cook
#
# ---------------------------------------------------------------------------
"""This is where my equations/things go."""


class myEquations(object):
    """
    My equations that do the things I want.

    Pass in a dictionary of initial parameters (initParams) that is then
    processed.

    This class has no bugs in it and always works the way I want it to.
    """

    def __init__(self, initParams):
        """Initialze myself and super class."""
        super().__init__()
        self.initParams = initParams

    def solve(self):
        """I solve things."""
        return ["Results1", "Results2", "Results3"]
