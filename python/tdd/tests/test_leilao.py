from unittest import TestCase
from src.leilao.excecoes import LanceInvalido
from src.leilao.dominio import Usuario, Lance, Leilao

# podemos rodar esse teste no terminal com python -m unittest src/leilao/test_leilao.py

# temos que sempre considerar cada caso de uso
class TestLeilao(TestCase):
    def setUp(self):
        """
        método padrão da classe TestCase, 
        é executado automaticamente antes de cada teste
        """
        self.gui = Usuario('gui', 500.0)

        self.lance_do_gui = Lance(self.gui, 150.0)

        self.leilao = Leilao('Celular')

    # o nome dos testes deve ser o mais descritivo possível, pois nunca chamamos ele pelo nome completo
    # então, o melhor nome é o que representa o que o teste faz
    # até porque se falhar, a ide mostra o nome do teste, assim te dando uma ideia do que está errado
    def test_deve_retornar_maior_e_menor_valor_quando_adicionados_em_ordem_crescente(self):
        # neste teste colocamos o menor lance primeiro
        yuri = Usuario('Yuri', 500.0)
        lance_do_yuri = Lance(yuri, 100.0)

        self.leilao.propoe(lance_do_yuri)
        self.leilao.propoe(self.lance_do_gui)

        menor_valor_esperado = 100
        maior_valor_esperado = 150
                            #valor esperado     #variavel a ser analisada
        self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)
        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)

    
    def test_nao_deve_permitir_propor_um_lance_em_ordem_decrescente(self):
        # neste teste colocamos o maior lance primeiro
        with self.assertRaises(LanceInvalido):
            yuri = Usuario('Yuri', 500.0)
            lance_do_yuri = Lance(yuri, 100.0)

            self.leilao.propoe(self.lance_do_gui)
            self.leilao.propoe(lance_do_yuri)

    def test_deve_retornar_o_mesmo_valor_para_o_menor_e_maior_lance_quando_leilao_tiver_apenas_um_lance(self):
        # neste teste teremos apenas um lance
        self.leilao.propoe(self.lance_do_gui)

                            #valor esperado     #variavel a ser analisada
        self.assertEqual(150, self.leilao.menor_lance)
        self.assertEqual(150, self.leilao.maior_lance)

    def test_deve_retornar_o_maior_e_o_menor_valor_quando_o_leilao_tiver_tres_lances(self):
        yuri = Usuario('Yuri', 500.0)
        vini = Usuario('Vini', 500.0)

        lance_do_vini = Lance(vini, 200.0)
        lance_do_yuri = Lance(yuri, 100.0)

        self.leilao.propoe(lance_do_yuri)
        self.leilao.propoe(self.lance_do_gui)
        self.leilao.propoe(lance_do_vini)

        menor_valor_esperado = 100
        maior_valor_esperado = 200
                            #valor esperado     #variavel a ser analisada
        self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)
        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)

    def test_deve_permitir_propor_um_lance_caso_o_leilao_nao_tenha_lances(self):
        self.leilao.propoe(self.lance_do_gui)

        self.assertEqual(1, len(self.leilao.lances))

    def test_deve_permitir_propor_um_lance_caso_o_ultimo_usuario_seja_diferente(self):
        yuri = Usuario('yuri', 500.0)
        lance_do_yuri = Lance(yuri, 200.0)

        self.leilao.propoe(self.lance_do_gui)
        self.leilao.propoe(lance_do_yuri)

        self.assertEqual(2, len(self.leilao.lances))

    def test_nao_deve_permitir_propor_lance_caso_o_usuario_seja_o_mesmo(self):
        lance_do_gui_200 = Lance(self.gui, 200.0)

        with self.assertRaises(LanceInvalido):
            self.leilao.propoe(self.lance_do_gui)
            self.leilao.propoe(lance_do_gui_200)
            self.assertEqual(1, len(self.leilao.lances))