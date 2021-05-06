# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Tela_Inicial.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Tela_Inicial(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(300, 250)
        MainWindow.setMinimumSize(QtCore.QSize(300, 250))
        MainWindow.setStyleSheet("background-color: rgb(99, 99, 99);\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_cabecalho = QtWidgets.QFrame(self.centralwidget)
        self.frame_cabecalho.setMaximumSize(QtCore.QSize(16777215, 70))
        self.frame_cabecalho.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_cabecalho.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_cabecalho.setObjectName("frame_cabecalho")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_cabecalho)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_Controle_estoque_pessoas = QtWidgets.QLabel(self.frame_cabecalho)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold SemiConden")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_Controle_estoque_pessoas.setFont(font)
        self.label_Controle_estoque_pessoas.setStyleSheet("color: rgb(230, 230, 230);\n"
"margin-left: 45px;\n"
"margin-right: 10px;\n"
"")
        self.label_Controle_estoque_pessoas.setObjectName("label_Controle_estoque_pessoas")
        self.horizontalLayout.addWidget(self.label_Controle_estoque_pessoas)
        self.verticalLayout.addWidget(self.frame_cabecalho)
        self.frame_opcoes = QtWidgets.QFrame(self.centralwidget)
        self.frame_opcoes.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_opcoes.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_opcoes.setObjectName("frame_opcoes")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_opcoes)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pushButton_cadastro = QtWidgets.QPushButton(self.frame_opcoes)
        self.pushButton_cadastro.setMinimumSize(QtCore.QSize(0, 50))
        self.pushButton_cadastro.setStyleSheet("QPushButton{\n"
"    border-radius: 5px;\n"
"    background-position: center;\n"
"    background-color: rgb(255, 85, 127);\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(50, 50, 50);\n"
"    color: rgb(200, 200, 200);\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(35, 35, 35);\n"
"    color: rgb(200, 200, 200);\n"
"}\n"
"\n"
"")
        self.pushButton_cadastro.setObjectName("pushButton_cadastro")
        self.verticalLayout_2.addWidget(self.pushButton_cadastro)
        self.pushButton_busca = QtWidgets.QPushButton(self.frame_opcoes)
        self.pushButton_busca.setMinimumSize(QtCore.QSize(0, 50))
        self.pushButton_busca.setStyleSheet("QPushButton{\n"
"    border-radius: 5px;\n"
"    background-position: center;\n"
"    background-color: rgb(255, 85, 127);\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(50, 50, 50);\n"
"    color: rgb(200, 200, 200);\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(35, 35, 35);\n"
"    color: rgb(200, 200, 200);\n"
"}\n"
"\n"
"")
        self.pushButton_busca.setObjectName("pushButton_busca")
        self.verticalLayout_2.addWidget(self.pushButton_busca)
        self.verticalLayout.addWidget(self.frame_opcoes)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_Controle_estoque_pessoas.setText(_translate("MainWindow", "Controle de Estoque de\n"
"           Pessoas :"))
        self.pushButton_cadastro.setText(_translate("MainWindow", "Cadastro"))
        self.pushButton_busca.setText(_translate("MainWindow", "Busca"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Tela_Inicial()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
