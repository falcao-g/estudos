import requests

class BuscaEndereco:
    def __init__(self, cep):
        cep = str(cep)
        if self.valida_cep(cep):
            self.cep = cep
        else:
            raise ValueError('CEP inválido')

    def __str__(self):
        return self.format()

    def valida_cep(self, cep):
        if len(cep) == 8:
            return True
        else:
            return False

    def format(self):
        return f"{self.cep[0:5]}-{self.cep[5:]}"

    def acessa_api(self):
        # acessa o https://brasilapi.com.br/ para pegar o endereço do CEP passado
        r = requests.get(f'https://brasilapi.com.br/api/cep/v1/{self.cep}')
        dados = r.json()
        return {
            dados['neighborhood'],
            dados['city'],
            dados['state'],
        }

cep = '19815340'
objeto_cep = BuscaEndereco(cep)
print(objeto_cep)

bairro, cidade, estado = objeto_cep.acessa_api()
print(bairro)
print(cidade)
print(estado)