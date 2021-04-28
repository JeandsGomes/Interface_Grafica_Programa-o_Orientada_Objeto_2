from unittest import TestCase, main
from cadastro import Cadastro
from pessoa import Pessoa

class Teste_Cadastro(TestCase):
    def test_Cadastro_existe(self):
        cadastro = Cadastro()

    def test_Cadastro_lista_pessoas_retorno_correto(self):
        cadastro = Cadastro()
        valor_esperado = []
        self.assertEqual(cadastro._lista_pessoas,valor_esperado)
    

    def test_Cadastro_cadastra_existe(self):
        pessoa = Pessoa('jeands','Av.PML',2,1)
        cadastro = Cadastro()
        cadastro.cadastra(pessoa)

    def test_Cadastro_cadastra_retorna_True(self):
        pessoa = Pessoa('jeands','Av.PML',2,1)
        cadastro = Cadastro()
        valor_esperado = True
        self.assertEqual(cadastro.cadastra(pessoa),valor_esperado)

    def test_Cadastro_cadastra_retorna_True(self):
        pessoa = Pessoa('jeands','Av.PML',2,1)
        cadastro = Cadastro()
        valor_esperado = False
        cadastro.cadastra(pessoa)
        self.assertEqual(cadastro.cadastra(pessoa),valor_esperado)

    def test_Cadastro_cadastra_retorna_valor_esperado(self):
        pessoa = Pessoa('jeands','Av.PML',2,1)
        cadastro = Cadastro()
        valor_esperado = [pessoa]
        cadastro.cadastra(pessoa)
        self.assertEqual(cadastro._lista_pessoas,valor_esperado)

    def test_Cadastro_busca_existe(self):
        cadastro = Cadastro()
        cadastro.busca(32)

    def test_Cadastro_busca_retorna_pessoa(self):
        pessoa = Pessoa('jeands','Av.PML',2,1)
        cadastro = Cadastro()
        valor_esperado = pessoa
        cadastro.cadastra(pessoa)
        self.assertEqual(cadastro.busca(2),valor_esperado)

    def test_Cadastro_cadastra_retorna_None(self):
        pessoa = Pessoa('jeands','Av.PML',2,1)
        cadastro = Cadastro()
        valor_esperado = None
        cadastro.cadastra(pessoa)
        self.assertEqual(cadastro.busca(3),valor_esperado)


if __name__ == "__main__":
    main()