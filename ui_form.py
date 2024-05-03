from PySide6.QtCore import QCoreApplication, QMetaObject, QRect, QSize
from PySide6.QtWidgets import (
    QGroupBox,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QMenuBar,
    QPushButton,
    QSizePolicy,
    QSpacerItem,
    QToolButton,
    QVBoxLayout,
    QWidget,
)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")
        MainWindow.resize(420, 275)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widget_2 = QWidget(self.centralwidget)
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout = QVBoxLayout(self.widget_2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QGroupBox(self.widget_2)
        self.groupBox.setObjectName("groupBox")
        self.groupBox.setMinimumSize(QSize(0, 70))
        self.horizontalLayout = QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.label.setMinimumSize(QSize(80, 0))

        self.horizontalLayout.addWidget(self.label)

        self.lineEdit = QLineEdit(self.groupBox)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setMinimumSize(QSize(200, 0))

        self.horizontalLayout.addWidget(self.lineEdit)

        self.toolButton = QToolButton(self.groupBox)
        self.toolButton.setObjectName("toolButton")
        self.toolButton.setMinimumSize(QSize(50, 0))

        self.horizontalLayout.addWidget(self.toolButton)

        self.verticalLayout.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(self.widget_2)
        self.groupBox_2.setObjectName("groupBox_2")
        self.groupBox_2.setMinimumSize(QSize(0, 70))
        self.horizontalLayout_2 = QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QLabel(self.groupBox_2)
        self.label_2.setObjectName("label_2")
        self.label_2.setMinimumSize(QSize(80, 0))

        self.horizontalLayout_2.addWidget(self.label_2)

        self.lineEdit_2 = QLineEdit(self.groupBox_2)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setMinimumSize(QSize(200, 0))

        self.horizontalLayout_2.addWidget(self.lineEdit_2)

        self.toolButton_2 = QToolButton(self.groupBox_2)
        self.toolButton_2.setObjectName("toolButton_2")
        self.toolButton_2.setMinimumSize(QSize(50, 0))

        self.horizontalLayout_2.addWidget(self.toolButton_2)

        self.verticalLayout.addWidget(self.groupBox_2)

        self.verticalLayout_2.addWidget(self.widget_2)

        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName("widget")
        self.horizontalLayout_3 = QHBoxLayout(self.widget)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalSpacer = QSpacerItem(
            309, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum
        )

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.pushButton = QPushButton(self.widget)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setMinimumSize(QSize(0, 50))

        self.horizontalLayout_3.addWidget(self.pushButton)

        self.verticalLayout_2.addWidget(self.widget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName("menubar")
        self.menubar.setGeometry(QRect(0, 0, 420, 17))
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(
            QCoreApplication.translate("MainWindow", "MainWindow", None)
        )
        self.groupBox.setTitle(
            QCoreApplication.translate("MainWindow", "\u5bfc\u5165", None)
        )
        self.label.setText(
            QCoreApplication.translate(
                "MainWindow", "\u6a21\u677f-\u8bfe\u7a0b-\u804c\u8d23\uff1a", None
            )
        )
        self.toolButton.setText(
            QCoreApplication.translate("MainWindow", "\u9009\u62e9", None)
        )
        self.groupBox_2.setTitle(
            QCoreApplication.translate("MainWindow", "\u5bfc\u51fa", None)
        )
        self.label_2.setText(
            QCoreApplication.translate(
                "MainWindow", "\u73ed\u7ea7-\u6559\u5e08-\u8bfe\u8868\uff1a", None
            )
        )
        self.toolButton_2.setText(
            QCoreApplication.translate("MainWindow", "\u9009\u62e9", None)
        )
        self.pushButton.setText(
            QCoreApplication.translate("MainWindow", "\u63d0\u4ea4", None)
        )

    # retranslateUi
