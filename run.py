"""Run the main functions of the program."""
import sys
from swearjar.InputOutput import initParams
from swearjar.GUI.guiWindow import GUIWindow
from PyQt5.QtWidgets import QApplication


def main():
    """Run simulation through GUI."""
    app = QApplication(sys.argv)
    ex = GUIWindow(initParams)
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
