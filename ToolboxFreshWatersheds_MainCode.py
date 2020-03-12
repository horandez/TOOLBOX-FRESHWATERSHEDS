import os
import sys
import inspect
from PyQt5.QtWidgets import QAction
from PyQt5.QtGui import QIcon
from .ToolboxFreshWatersheds_UserInterface import ToolboxFreshWatersheds

cmd_folder = os.path.split(inspect.getfile(inspect.currentframe()))[0]

class ToolboxFreshWatershedsPlugin:
    def _init_(self, iface)
        self.iface = iface
        
    def initGui(self):
        icon = os.path.join(os.path.join(cmd_folder,'logo.png'))
        self.action = QAction(QIcon(icon), 'ToolboxFreshWatersheds V1.0', self.iface.mainWindow())
        self.action.triggered.connect(self.run)
        self.iface.addPluginToMenu('&Toolbox FreshWatersheds', self.action)
        self.iface.addToolBarIcon(self.action)
        self.first_start = True
        
    def unload(self):
        self.iface.removeToolBarIcon(self.action)
        self.iface.removePluginMenu('&Toolbox FreshWatersheds', self.action)  
        del self.action
        
    def run(self):
        if self.first_start == True:
            self.first_start = False
            self.dlg = ToolboxFreshWatersheds()
        self.dlg.show()