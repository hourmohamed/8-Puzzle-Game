# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gui.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1400, 581)
        self.gridLayoutWidget = QWidget(Form)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(110, 80, 481, 431))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 1, 1, 1, 1)

        self.label_5 = QLabel(self.gridLayoutWidget)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 1, 2, 1, 1)

        self.label_3 = QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)

        self.label_1 = QLabel(self.gridLayoutWidget)
        self.label_1.setObjectName(u"label_1")

        self.gridLayout.addWidget(self.label_1, 0, 1, 1, 1)

        self.label_0 = QLabel(self.gridLayoutWidget)
        self.label_0.setObjectName(u"label_0")

        self.gridLayout.addWidget(self.label_0, 0, 0, 1, 1)

        self.label_6 = QLabel(self.gridLayoutWidget)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 2, 0, 1, 1)

        self.label_7 = QLabel(self.gridLayoutWidget)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout.addWidget(self.label_7, 2, 1, 1, 1)

        self.label_8 = QLabel(self.gridLayoutWidget)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout.addWidget(self.label_8, 2, 2, 1, 1)

        self.label_2 = QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 0, 2, 1, 1)

        self.bfs_button = QPushButton(Form)
        self.bfs_button.setObjectName(u"bfs_button")
        self.bfs_button.setGeometry(QRect(700, 280, 111, 41))
        self.dfs_button = QPushButton(Form)
        self.dfs_button.setObjectName(u"dfs_button")
        self.dfs_button.setGeometry(QRect(700, 340, 111, 41))
        self.manh_button = QPushButton(Form)
        self.manh_button.setObjectName(u"manh_button")
        self.manh_button.setGeometry(QRect(700, 400, 111, 41))
        self.eucli_button = QPushButton(Form)
        self.eucli_button.setObjectName(u"eucli_button")
        self.eucli_button.setGeometry(QRect(700, 460, 111, 41))
        self.lineEdit = QLineEdit(Form)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(740, 50, 113, 21))
        self.label_9 = QLabel(Form)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(610, 50, 121, 31))
        self.depth_label = QLabel(Form)
        self.depth_label.setObjectName(u"depth_label")
        self.depth_label.setGeometry(QRect(620, 90, 81, 31))
        self.path_label = QLabel(Form)
        self.path_label.setObjectName(u"path_label")
        self.path_label.setGeometry(QRect(620, 130, 61, 21))
        self.nodes_label = QLabel(Form)
        self.nodes_label.setObjectName(u"nodes_label")
        self.nodes_label.setGeometry(QRect(620, 170, 101, 21))
        self.cost_label = QLabel(Form)
        self.cost_label.setObjectName(u"cost_label")
        self.cost_label.setGeometry(QRect(630, 200, 51, 20))
        self.depth_disp_label = QLabel(Form)
        self.depth_disp_label.setObjectName(u"depth_disp_label")
        self.depth_disp_label.setGeometry(QRect(750, 90, 49, 16))
        self.path_disp_label = QLabel(Form)
        self.path_disp_label.setObjectName(u"path_disp_label")
        self.path_disp_label.setGeometry(QRect(750, 130, 651, 31))
        self.nodes_disp_label = QLabel(Form)
        self.nodes_disp_label.setObjectName(u"nodes_disp_label")
        self.nodes_disp_label.setGeometry(QRect(750, 170, 49, 16))
        self.cost_disp_label = QLabel(Form)
        self.cost_disp_label.setObjectName(u"cost_disp_label")
        self.cost_disp_label.setGeometry(QRect(750, 210, 49, 16))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_4.setText("")
        self.label_5.setText("")
        self.label_3.setText("")
        self.label_1.setText("")
        self.label_0.setText("")
        self.label_6.setText("")
        self.label_7.setText("")
        self.label_8.setText("")
        self.label_2.setText("")
        self.bfs_button.setText(QCoreApplication.translate("Form", u"BFS", None))
        self.dfs_button.setText(QCoreApplication.translate("Form", u"DFS", None))
        self.manh_button.setText(QCoreApplication.translate("Form", u"A*- MANH", None))
        self.eucli_button.setText(QCoreApplication.translate("Form", u"A*-EUCLI", None))
        self.label_9.setText(QCoreApplication.translate("Form", u" Enter initial state", None))
        self.depth_label.setText(QCoreApplication.translate("Form", u"Search Depth:", None))
        self.path_label.setText(QCoreApplication.translate("Form", u"  Path:", None))
        self.nodes_label.setText(QCoreApplication.translate("Form", u"Expanded Nodes:", None))
        self.cost_label.setText(QCoreApplication.translate("Form", u" Cost:", None))
        self.depth_disp_label.setText("")
        self.path_disp_label.setText("")
        self.nodes_disp_label.setText("")
        self.cost_disp_label.setText("")
    # retranslateUi

