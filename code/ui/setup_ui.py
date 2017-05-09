# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'setup_ui.ui'
#
# Created by: PyQt4 UI code generator 4.12
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(324, 272)
        self.gridLayout = QtGui.QGridLayout(Dialog)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setMinimumSize(QtCore.QSize(75, 0))
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.app_lineEdit = QtGui.QLineEdit(Dialog)
        self.app_lineEdit.setObjectName(_fromUtf8("app_lineEdit"))
        self.horizontalLayout.addWidget(self.app_lineEdit)
        self.horizontalLayout_3.addLayout(self.horizontalLayout)
        self.appicon_pushButton = QtGui.QPushButton(Dialog)
        self.appicon_pushButton.setMinimumSize(QtCore.QSize(107, 0))
        self.appicon_pushButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.appicon_pushButton.setObjectName(_fromUtf8("appicon_pushButton"))
        self.horizontalLayout_3.addWidget(self.appicon_pushButton)
        self.gridLayout.addLayout(self.horizontalLayout_3, 0, 0, 1, 3)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_2.addWidget(self.label_2)
        self.group_lineEdit = QtGui.QLineEdit(Dialog)
        self.group_lineEdit.setObjectName(_fromUtf8("group_lineEdit"))
        self.horizontalLayout_2.addWidget(self.group_lineEdit)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_2)
        self.groupicon_pushButton = QtGui.QPushButton(Dialog)
        self.groupicon_pushButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.groupicon_pushButton.setObjectName(_fromUtf8("groupicon_pushButton"))
        self.horizontalLayout_4.addWidget(self.groupicon_pushButton)
        self.gridLayout.addLayout(self.horizontalLayout_4, 1, 0, 1, 3)
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.windows_lineEdit = QtGui.QLineEdit(Dialog)
        self.windows_lineEdit.setObjectName(_fromUtf8("windows_lineEdit"))
        self.gridLayout.addWidget(self.windows_lineEdit, 2, 1, 1, 2)
        self.label_4 = QtGui.QLabel(Dialog)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.linux_lineEdit = QtGui.QLineEdit(Dialog)
        self.linux_lineEdit.setObjectName(_fromUtf8("linux_lineEdit"))
        self.gridLayout.addWidget(self.linux_lineEdit, 3, 1, 1, 2)
        self.label_5 = QtGui.QLabel(Dialog)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)
        self.mac_lineEdit = QtGui.QLineEdit(Dialog)
        self.mac_lineEdit.setObjectName(_fromUtf8("mac_lineEdit"))
        self.gridLayout.addWidget(self.mac_lineEdit, 4, 1, 1, 2)
        self.acceptdrops_checkBox = QtGui.QCheckBox(Dialog)
        self.acceptdrops_checkBox.setObjectName(_fromUtf8("acceptdrops_checkBox"))
        self.gridLayout.addWidget(self.acceptdrops_checkBox, 5, 0, 1, 1)
        self.ok_pushButton = QtGui.QPushButton(Dialog)
        self.ok_pushButton.setObjectName(_fromUtf8("ok_pushButton"))
        self.gridLayout.addWidget(self.ok_pushButton, 5, 1, 1, 1)
        self.cancel_pushButton = QtGui.QPushButton(Dialog)
        self.cancel_pushButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.cancel_pushButton.setObjectName(_fromUtf8("cancel_pushButton"))
        self.gridLayout.addWidget(self.cancel_pushButton, 5, 2, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.label.setText(_translate("Dialog", "App Title", None))
        self.appicon_pushButton.setText(_translate("Dialog", "App Icon", None))
        self.label_2.setText(_translate("Dialog", "Group Name", None))
        self.groupicon_pushButton.setText(_translate("Dialog", "Group Icon", None))
        self.label_3.setText(_translate("Dialog", "Windows Exec", None))
        self.label_4.setText(_translate("Dialog", "Linux Exec", None))
        self.label_5.setText(_translate("Dialog", "Mac Exec", None))
        self.acceptdrops_checkBox.setText(_translate("Dialog", "Accept Drops", None))
        self.ok_pushButton.setText(_translate("Dialog", "OK", None))
        self.cancel_pushButton.setText(_translate("Dialog", "Cancel", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

