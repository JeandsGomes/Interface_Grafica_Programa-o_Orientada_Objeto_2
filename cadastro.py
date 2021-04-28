class Cadastro():
    def __init__(self):
        self._lista_pessoas = []

    def cadastra(self,pessoa):
        self._lista_pessoas.append(pessoa)
        return True

    def busca(self,cpf):
        for lp in self._