from src.leilao.excecoes import LanceInvalido
from src.leilao.dominio import Leilao, Usuario

import pytest

#podemos rodar os testes no terminal com o comando: pytest

#isso avisa o pytest que os testes precisam dessa função, fazendo eles poderem receber a função como parametro
@pytest.fixture
def vini():
    return Usuario('vini', 100.0)

@pytest.fixture
def leilao():
    return Leilao('Celular')
                                                                                #isso indica que esse teste precisa da função vini
def test_deve_subtrair_valor_da_carteira_do_usuario_quando_este_propor_um_lance(vini, leilao):
    vini.propoe_lance(leilao, 50.0)

    assert vini.carteira == 50.0

def test_deve_permitir_propor_lance_quando_o_valor_e_menor_que_o_da_carteira(vini, leilao):
    vini.propoe_lance(leilao, 50.0)

    assert vini.carteira == 50.0

def test_deve_permitir_propor_lance_quando_o_valor_e_igual_ao_valor_da_carteira(vini, leilao):
    vini.propoe_lance(leilao, 100.0)

    assert vini.carteira == 0.0

def test_nao_deve_permitir_propor_lance_quando_o_valor_e_maior_que_o_da_carteira(vini, leilao):
    #espera que ocorra um erro, caso isso não aconteça, o teste falha
    with pytest.raises(LanceInvalido):
        vini.propoe_lance(leilao, 150.0)

        assert vini.carteira == 100.0