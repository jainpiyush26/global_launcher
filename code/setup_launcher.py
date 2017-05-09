#! /usr/bin/pythonw
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys
import ui.setup_ui as launcher_ui
import json
import os
import re

JSON_LOCATION = os.path.join(os.path.dirname("__file__"), "../", "resources", "app_json")
ICON_LOCATION = os.path.join(os.path.dirname("__file__"), "../", "resources", "icon_collection")
DEFAULT_JSON_OBJECT = {"app": "",
                       "app_name": "",
                       "app_icon": "default.png",
                       "group_name": "",
                       "group_icon": "default.png",
                       "app_executable": {"windows": "",
                                          "linux": "",
                                          "darwin": ""},
                       "accept_drops": False
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
        self.app_lineEdit.textEdited.connect(self.enable_app_icon)
        self.group_lineEdit.textEdited.connect(self.enable_group_icon)
        self.appicon_pushButton.clicked.connect(lambda: self.get_icon_path("app"))
        self.groupicon_pushButton.clicked.connect(lambda: self.get_icon_path("group"))
        self.cancel_pushButton.clicked.connect(self.close)
        self.windows_lineEdit.textEdited.connect(self.executable_populate)
        self.mac_lineEdit.textEdited.connect(self.executable_populate)
        self.linux_lineEdit.textEdited.connect(self.executable_populate)

        self.app_json = DEFAULT_JSON_OBJECT


    def acceptDrops(self):
        if self.acceptdrops_checkBox.isChecked():
            self.accept_drop = True
        else:
            self.accept_drop = False

    def enable_app_icon(self):
        self.appicon_pushButton.setEnabled(True)
        self.app_name = str(self.app_lineEdit.text())
        self.group_lineEdit.setEnabled(True)

    def enable_group_icon(self):
        self.groupicon_pushButton.setEnabled(True)
        self.group_name = str(self.group_lineEdit.text())

    def get_icon_path(self, counter):
        if counter == "app":
            self.app_icon_path = QFileDialog.getOpenFileName(self, "Select Icons", filter="Images (*.png *.ico)")
            self.appicon_pushButton.setIcon(QIcon(self.app_icon_path))
            self.appicon_pushButton.setIconSize(QSize(10, 10))
        elif counter == "group":
            self.group_icon_path = QFileDialog.getOpenFileName(self, "Select Icons", filter="Images (*.png *.ico)")
            self.groupicon_pushButton.setIcon(QIcon(self.group_icon_path))
            self.groupicon_pushButton.setIconSize(QSize(10, 10))

    def executable_populate(self):
        if self.sender().objectName() == "windows_lineEdit":
            self.windows_exec = str(self.sender().text()).replace('"', "")

        if self.sender().objectName() == "linux_lineEdit":
            self.linux_exec = str(self.sender().text()).replace('"', "")

        if self.sender().objectName() == "mac_lineEdit":
            self.mac_exec = str(self.sender().text()).replace('"', "")

        self.ok_pushButton.setEnabled(True)

    def initialize_ui(self, counter):
        self.ok_pushButton.setEnabled(counter)
        self.appicon_pushButton.setEnabled(counter)
        self.group_lineEdit.setEnabled(counter)
        self.groupicon_pushButton.setEnabled(counter)

    def save_config_file(self):
        self.app_json["app"] = self.app_name
        self.app_json["app_name"] = re.replace("[ \S]")

        self.close()


def main():
    app_obj = QApplication(sys.argv)
    launcher_setup_window = SetupLauncher()
    launcher_setup_window.show()
    app_obj.exec_()

if __name__ == "__main__":
    main()
