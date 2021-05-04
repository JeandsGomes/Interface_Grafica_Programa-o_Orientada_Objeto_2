from unittest import TestCase, main
from pessoa import Pessoa

class Teste_Pessa(TestCase):

    def test_pessoa_existe(self):
        pessoa = Pessoa('jeands','Av.PML',2,1)

    def test_pessoa_get_nome_existe(self):
        pessoa = Pessoa('jeands','Av.PML',2,1)
        pessoa.nome

    def test_pessoa_get_nome_retorno_esperado(self):
        pessoa = Pessoa('jeands','Av.PML',2,1)
        valor_esperado = 'jeands'
        self.assertEqual(pessoa.nome,valor_esperado)

    def test_pessoa_get_endereco_existe(self):
        pessoa = Pessoa('jeands','Av.PML',2,1)
        pessoa.endereco

    def test_pessoa_get_endereco_retorno_esperado(self):
        pessoa = Pessoa('jeands','Av.PML',2,1)
        valor_esperado = 'Av.PML'
        self.assertEqual(pessoa.endereco,valor_esperado)

    def test_pessoa_get_cpf_existe(self):
        pessoa = Pessoa('jeands','Av.PML',2,1)
        pessoa.cpf

    def test_pessoa_get_cpf_retorno_esperado(self):
        pessoa = Pessoa('jeands','Av.PML',2,1)
        valor_esperado = 2
        self.assertEqual(pessoa.cpf,valor_esperado)

    def test_pessoa_get_nascimento_existe(self):
        pessoa = Pessoa('jeands','Av.PML',2,1)
        pessoa.nascimento

    def test_pessoa_get_nascimento_retorno_esperado(self):
        pessoa = Pessoa('jeands','Av.PML',2,1)
        valor_esperado = 1
        self.assertEqual(pessoa.nascimento,valor_esperado)


if __name__ == "__main__":
    main()