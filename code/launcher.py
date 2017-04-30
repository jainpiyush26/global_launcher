#! /usr/bin/python
from PySide.QtCore import *
from PySide.QtGui import *
import os
import sys
import json

# Generate the resource path
RESOURCES_PATH = os.path.join(os.path.dirname(__file__), "../", "resources")


class GlobalLauncher(QDialog):
    # global launcher main class
    def __init__(self):
        super(GlobalLauncher, self).__init__()
        self.icon_path = os.path.join(RESOURCES_PATH, "icon_collection")
        self.setWindowFlags(Qt.SplashScreen)

        # Setting up the system tray icon
        self.system_tray_icon = QSystemTrayIcon(self)
        self.system_tray_icon.setIcon(QIcon(os.path.join(self.icon_path, "launch.png")))
        self.system_tray_icon.setVisible(True)

        # Calling the basic functions
        self.setup_system_tray_icon()

    def setVisible(self, value):
        super(GlobalLauncher, self).setVisible(False)

    def setup_system_tray_icon(self):
        self.global_launcher_main_menu = QMenu()
        self.close_action = QAction("Close", self, triggered=self.close)
        self.close_action.setIcon(QIcon(os.path.join(self.icon_path, "default.png")))
        self.global_launcher_main_menu.addAction(self.close_action)


        self.system_tray_icon.setContextMenu(self.global_launcher_main_menu)

    def prepare_app_actions(self):
        pass

    def closeEvent(self, event):
        event.accept()
        sys.exit()


def main():
    launcherwindow = GlobalLauncher()
    launcherwindow.show()

    app.exec_()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    if QSystemTrayIcon.isSystemTrayAvailable():
        main()
    else:
        # This is redundant!
        print "You do not have systemtray icon!"