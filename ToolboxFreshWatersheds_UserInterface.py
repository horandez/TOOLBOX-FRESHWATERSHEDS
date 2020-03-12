import os

from PyQt5 import uic
from PyQt5 import QtWidgets

FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'ToolboxFreshWatersheds_UserInterface.ui'))


class ToolboxFreshWatersheds(QtWidgets.QDialog, FORM_CLASS):
    def __init__(self, parent=None):
        super(ToolboxFreshWatersheds, self).__init__(parent)
        self.setupUi(self)