from datetime import datetime, timedelta

class DatasBr:
    def __init__(self):
        self.momento_cadastro = datetime.today()

    def mes_cadastro(self):
        meses_do_ano = [
            "janeiro", "fevereiro", "março",
            "abril", "maio", "junho",
            "julho", "agosto", "setembro",
            "outubro", "novembro", "dezembro"
        ]

        mes_cadastro = self.momento_cadastro.month -1
        return meses_do_ano[mes_cadastro]

    def dia_semana(self):
        dia_semana_lista = [
            "segunda", "terça",
            "quarta", "quinta", "sexta",
            "sábado", "domingo"
        ]

        dia_semana = self.momento_cadastro.weekday()
        return dia_semana_lista[dia_semana]

    def format(self):
        return self.momento_cadastro.strftime("%d/%m/%Y %H:%M")

    def tempo_cadastro(self):
        return (datetime.today() + timedelta(days=30)) - self.momento_cadastro

    def __str__(self):
        return self.format()

cadastro = DatasBr()
print(cadastro)
print(cadastro.momento_cadastro)
print(cadastro.mes_cadastro())
print(cadastro.dia_semana())
print(cadastro.tempo_cadastro())
