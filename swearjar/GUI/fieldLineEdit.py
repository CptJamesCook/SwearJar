"""Used for input in the GUI."""
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QDoubleValidator


class fieldLineEdit(QLineEdit):
    """Used for input in the GUI."""

    changePic = pyqtSignal()

    def __init__(self, name=None, parent=None):
        """Initialize self and super class."""
        super().__init__(parent)
        self.name = name
        validator = QDoubleValidator()
        validator.setRange(-1000000, 1000000, 5)
        self.setValidator(validator)

    def value(self):
        """Return the value of the text box as a float."""
        if self.hasAcceptableInput():
            return float(self.text())
        return None

    def setValue(self, val):
        """Set the value parameter of the fieldLineEdit box."""
        self.setText(str(val))

    def mousePressEvent(self, event):
        """Emit a change picture signal upon clicking the field."""
        self.changePic.emit()
