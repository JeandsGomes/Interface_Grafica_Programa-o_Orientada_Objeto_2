class Cadastro():
    def __init__(self):
        self._lista_pessoas = []

    def cadastra(self,pessoa):
        existe = self.busca(pessoa.cpf)
        if(existe == None):
            self._lista_pessoas.append(pessoa)
            return True
        return False

    def busca(self,cpf):
        for lp in self._lista_pessoas:
            if(lp.cpf == cpf):
                return lp
        return None