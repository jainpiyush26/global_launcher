#!/usr/local/bin/pythonw
from PySide.QtCore import *
from PySide.QtGui import *
import os
import sys
import json
from subprocess import Popen
from collections import defaultdict

# Generate the resource path
RESOURCES_PATH = os.path.join(os.path.dirname(__file__), "../", "resources")


class dropDialog(QDialog):
    """
    Launches a small dialog for dragging and dropping the application's inputs
    """
    def __init__(self, parent=None):
        super(dropDialog, self).__init__(parent=None)
        self.parent = parent
        self.parent_geometry = self.parent.system_tray_icon.geometry()
        if sys.platform == "darwin":
            self.setGeometry(QRect(self.parent_geometry.x(), self.parent_geometry.y() + 30, 60, 60))
        else:
            self.setGeometry(QRect(self.parent_geometry.x(), self.parent_geometry.y() + 110, 60, 60))
        self.setWindowFlags(Qt.SplashScreen | Qt.WindowStaysOnTopHint)
        # self.setAttribute(Qt.WA_TintedBackground)
        self.setStyleSheet("background-color: rgba(255, 255, 255, 100);")
        self.layout = QHBoxLayout()
        self.label = QLabel(self)
        pixmap = QPixmap(os.path.join(self.parent.icon_path, "drop.png"))
        self.label.setPixmap(pixmap.scaled(50, 50, Qt.KeepAspectRatio))
        self.layout.addWidget(self.label)
        self.setLayout(self.layout)
        self.setAcceptDrops(True)

    def dragEnterEvent(self, event):
        event.accept()

    def dropEvent(self, event):
        self.parent.drop_data = str(event.mimeData().urls()[0].toLocalFile())
        self.close()

    def mouseDoubleClickEvent(self, event):
        self.parent.drop_data = None
        self.close()


class GlobalLauncher(QDialog):
    # global launcher main class
    def __init__(self):
        super(GlobalLauncher, self).__init__()
        self.icon_path = os.path.join(RESOURCES_PATH, "icon_collection")
        self.setWindowFlags(Qt.SplashScreen)

        self.drop_data = ""
        self.app_action_dict = {}
        self.menu_submenu_dict = defaultdict(list)

        # Setting up the system tray icon
        self.system_tray_icon = QSystemTrayIcon(self)
        self.system_tray_icon.setIcon(QIcon(os.path.join(self.icon_path, "app.png")))
        self.system_tray_icon.setVisible(True)

        # Calling the basic functions
        self.setup_system_tray_icon()

    def setVisible(self, value):
        super(GlobalLauncher, self).setVisible(False)

    def setup_system_tray_icon(self):
        self.global_launcher_main_menu = QMenu()
        self.prepare_app_actions()
        self.close_action = QAction("Close", self, triggered=self.close)
        self.close_action.setIcon(QIcon(os.path.join(self.icon_path, "close.png")))
        self.global_launcher_main_menu.addAction(self.close_action)

        self.system_tray_icon.setContextMenu(self.global_launcher_main_menu)

    def prepare_app_actions(self):
        self.app_json_folder = os.path.join(RESOURCES_PATH, "app_json")
        json_files = [os.path.join(self.app_json_folder, items) for items in os.listdir(self.app_json_folder) if items.endswith(".json") and items != 'sample.json']
        for json_file in json_files:
            try:
                with open(json_file) as file_open:
                    json_python_obj = json.load(file_open)
            except:
                continue
            if json_python_obj["app"].strip() != "":
                if json_python_obj["group"].strip() != "":
                    self.menu_submenu_dict[json_python_obj["group"].strip()].append(json_python_obj)
                else:
                    self.menu_submenu_dict["BASE"].append(json_python_obj)
            else:
                continue
        for submenu_names in self.menu_submenu_dict.keys():
            submenu = QMenu(submenu_names)
            submenu.setIcon(QIcon(os.path.join(self.icon_path, self.menu_submenu_dict[submenu_names][0]["group_icon"])))
            for apps in self.menu_submenu_dict[submenu_names]:
                if apps["app_executable"][sys.platform.lower()].strip() != '' and os.path.exists(apps["app_executable"][sys.platform.lower()].strip()):
                    action = QAction(apps["app"], self, triggered=self.perform_action)
                    action.setIcon(QIcon(os.path.join(self.icon_path, str(apps["app_icon"]))))
                    submenu.addAction(action)
                    self.app_action_dict[str(apps["app"])] = [str(apps["app_executable"][sys.platform.lower()]).strip(), apps["accept_drops"]]
                else:
                    continue
            self.global_launcher_main_menu.addMenu(submenu)

    def perform_action(self):
        sender_app_name = str(self.sender().text())
        application_location = self.app_action_dict[sender_app_name][0]
        application_accept_drop = self.app_action_dict[sender_app_name][1]
        if application_accept_drop:
            drop_ui = dropDialog(self)
            drop_ui.exec_()
        if self.drop_data:
            Popen("{} {}".format(application_location, self.drop_data), shell=True)
        else:
            Popen("{}".format(application_location), shell=True)

    def closeEvent(self, event):
        print "closing system tray"
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