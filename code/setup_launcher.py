#! /usr/bin/pythonw
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys
import ui.setup_ui as launcher_ui
import json
import os

JSON_LOCATION = os.path.join(os.path.dirname("__file__"), "../", "resources", "app_json")
ICON_LOCATION = os.path.join(os.path.dirname("__file__"), "../", "resources", "icon_collection")
DEFAULT_JSON_OBJECT = {"app": "",
                       "app_name": "",
                       "app_icon": "",
                       "group_name": "",
                       "group_icon": "",
                       "app_executable": {"windows": "",
                                          "linux": "",
                                          "darwin": ""}
                       }


class SetupLauncher(launcher_ui.Ui_Dialog, QDialog):
    def __init__(self, parent=None):
        super(SetupLauncher, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Setup Launcher Applications")
        self.setWindowIcon(QIcon(os.path.join(ICON_LOCATION, "launch.png")))

        # Initial function
        self.initialize_ui(False)
        # Signal Slots
        self.app_lineEdit.editingFinished.connect(lambda: self.initialize_ui(True))
        self.appicon_pushButton.clicked.connect(lambda: self.get_icon_path("app"))
        self.groupicon_pushButton.clicked.connect(lambda: self.get_icon_path("group"))
        self.cancel_pushButton.clicked.connect(self.close)

    def get_icon_path(self, counter):
        if counter == "app":
            self.app_icon_path = QFileDialog.getOpenFileName(self, "Select Icons", filter="Images (*.png *.ico)")
            self.appicon_pushButton.setIcon(QIcon(self.app_icon_path))
            self.appicon_pushButton.setIconSize(QSize(10, 10))
        elif counter == "group":
            self.group_icon_path = QFileDialog.getOpenFileName(self, "Select Icons", filter="Images (*.png *.ico)")
            self.groupicon_pushButton.setIcon(QIcon(self.group_icon_path))
            self.groupicon_pushButton.setIconSize(QSize(10, 10))


    def initialize_ui(self, counter):
        self.ok_pushButton.setEnabled(counter)
        self.appicon_pushButton.setEnabled(counter)
        self.group_lineEdit.setEnabled(counter)
        self.groupicon_pushButton.setEnabled(counter)

def main():
    app_obj = QApplication(sys.argv)
    launcher_setup_window = SetupLauncher()
    launcher_setup_window.show()
    app_obj.exec_()

if __name__ == "__main__":
    main()
