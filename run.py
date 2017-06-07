# ---------------------------------------------------------------------------
#
#  ExampleGUI: An example GUI for the ESDLab.
#
#  Copyright (C) 2017 by Energy Systems Design Laboratory, University of Alberta
#
#  This software is distributed under the MIT License.
#  For more information, see LICENSE.txt file
#
#  - Description: Runs the GUI.
#  - Developers: J. Cook
#
# ---------------------------------------------------------------------------
"""Run the main functions of the program."""
import sys
from examplegui.InputOutput import initParams
from examplegui.GUI.guiWindow import GUIWindow
from PyQt5.QtWidgets import QApplication


def main():
    """Run simulation through GUI."""
    app = QApplication(sys.argv)
    ex = GUIWindow(initParams)
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
