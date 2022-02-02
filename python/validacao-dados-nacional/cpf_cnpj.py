from validate_docbr import CPF, CNPJ

# Factory method, uma classe mãe (superclasse) que decide qual classe fila (subclasse) vai instanciar,
# retorna um objeto CPF ou CNPJ com base na quantidade de dígitos
# Podemos observar também que aqui é possível se usar polimorfismo, pois o CPF e CNPJ tem as mesmas funções
class Documento:
    @staticmethod
    def cria_documento(documento):
        if len(documento) == 11:
            return DocCpf(documento)
        elif len(documento) == 14:
            return DocCnpj(documento)
        else:
            raise ValueError("Quantidade de dígitos incorreta!")

class DocCpf:
    def __init__(self, documento):
        if self.valida(documento):
            self.cpf = documento
        else:
            raise ValueError("Cpf inválido!")

    def __str__(self):
        return self.format()

    def valida(self, documento):
        validador = CPF()
        return validador.validate(documento)

    def format(self):
      mascara = CPF()
      return mascara.mask(self.cpf)

class DocCnpj:
    def __init__(self, documento):
        if self.valida(documento):
            self.cnpj = documento
        else:
            raise ValueError("Cnpj inválido!")

    def __str__(self):
        return self.format()

    def valida(self, documento):
        mascara = CNPJ()
        return mascara.validate(documento)

    def format(self):
        mascara = CNPJ()
        return mascara.mask(self.cnpj)

exemplo_cnpj = "35379838000112"
exemplo_cpf = "01234567890"

documento = Documento.cria_documento(exemplo_cpf)
print(documento)

documento = Documento.cria_documento(exemplo_cnpj)
print(documento)