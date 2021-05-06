import sys
import os

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QMessageBox
from PyQt5.QtCore import QCoreApplication

from Tela_Inicial import Tela_Inicial
from Cadastroa import Tela_Cadastro
from Busca import Tela_Busca
from cadastro import Cadastro
from pessoa import Pessoa

class Ui_Main(QtWidgets.QWidget):
    def setupUi(self, Main):
        Main.setObjectName('Main')
        Main.resize(640, 480)

        self.QtStack = QtWidgets.QStackedLayout()

        self.stack0 = QtWidgets.QMainWindow()
        self.stack1 = QtWidgets.QMainWindow()
        self.stack2 = QtWidgets.QMainWindow()

        self.tela_inicial = Tela_Inicial()
        self.tela_inicial.setupUi(self.stack0)

        self.tela_cadastro = Tela_Cadastro()
        self.tela_cadastro.setupUi(self.stack1)

        self.tela_buscar = Tela_Busca()
        self.tela_buscar.setupUi(self.stack2)

        self.QtStack.addWidget(self.stack0)
        self.QtStack.addWidget(self.stack1)
        self.QtStack.addWidget(self.stack2)

class Main(QMainWindow, Ui_Main):
    def __init__(self,parent=None):
        super(Main, self).__init__(parent)
        self.setupUi(self)

        self.cadastro = Cadastro()
        self.tela_inicial.pushButton_cadastro.clicked.connect(self.abrirTelaCadastro)
        self.tela_inicial.pushButton_busca.clicked.connect(self.abrirTelaBusca)


        self.tela_cadastro.pushButton_cadastro_cadastrar.clicked.connect(self.botaoCadastra)

        self.tela_buscar.pushButton_busca_buscar.clicked.connect(self.botaoBusca)
        self.tela_buscar.pushButton_voltar.clicked.connect(self.abrirTelaInicial)

    def botaoCadastra(self):
        nome = self.tela_cadastro.lineEdit_cadastro_nome.text()
        endereco = self.tela_cadastro.lineEdit_cadastro_endereco.text()
        cpf = self.tela_cadastro.lineEdit_cadastro_cpf.text()
        nascimento = self.tela_cadastro.lineEdit_cadastro_nascimento.text()
        if not(nome == '' or endereco == '' or cpf == '' or nascimento == '') :
            pessoa = Pessoa(nome,endereco,cpf,nascimento)
            if (self.cadastro.cadastra(pessoa)):
                QMessageBox.information(None,'POOII','Cadastro realizado com sucesso!')
                #Apagar os campos apos cadastrar
                self.tela_cadastro.lineEdit_cadastro_nome.setText('')
                self.tela_cadastro.lineEdit_cadastro_endereco.setText('')
                self.tela_cadastro.lineEdit_cadastro_cpf.setText('')
                self.tela_cadastro.lineEdit_cadastro_nascimento.setText('')
            else:
                QMessageBox.information(None,'POOII','O CPF informado já está cadastrado na base de dados')
        else:
            QMessageBox.information(None,'POOII','Todos os valores deven ser preenchidos!')
        
        self.QtStack.setCurrentIndex(0)



    def botaoBusca(self):
        cpf = self.tela_buscar.lineEdit_busca_cpf.text()
        pessoa = self.cadastro.busca(cpf)
        if (pessoa!=None):
            self.tela_buscar.lineEdit_busca_nome.setText(pessoa.nome)
            self.tela_buscar.lineEdit_busca_endereco.setText(pessoa.endereco)
            self.tela_buscar.lineEdit_busca_nascimento.setText(pessoa.nascimento)
            #QMessageBox.information(None,'POOII','Nome: {}\nEndereco: {}\nNascimento: {}'.format(pessoa.nome,pessoa.endereco,pessoa.nascimento))
        else:
            QMessageBox.information(None,'POOII','CPF informado não cadastrado')
            self.tela_buscar.lineEdit_busca_nome.setText('')
            self.tela_buscar.lineEdit_busca_endereco.setText('')
            self.tela_buscar.lineEdit_busca_nascimento.setText('')
        
    def abrirTelaCadastro(self):
        self.QtStack.setCurrentIndex(1)

    def abrirTelaBusca(self):
        self.QtStack.setCurrentIndex(2)

    def abrirTelaInicial(self):
        self.QtStack.setCurrentIndex(0)

if __name__=='__main__':
    app = QApplication(sys.argv)
    show_main = Main()
    sys.exit(app.exec_())

