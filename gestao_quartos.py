class Quarto:
    def __init__(self, numero, tipo):
        self.numero = numero
        self.tipo = tipo
        self.reservado = False
        self.hospede = None

class GestaoQuartos:
    def __init__(self):
        self.quartos = []

    def adicionar_quartos(self, tipo, quantidade):
        numero_inicial = len(self.quartos) + 1
        for i in range(quantidade):
            self.quartos.append(Quarto(numero_inicial + i, tipo))

    def listar_quartos(self):
        return self.quartos

    def buscar_quartos_disponiveis(self):
        return [quarto for quarto in self.quartos if not quarto.reservado]

# Exemplo de uso:
# gestao_quartos = GestaoQuartos()
# gestao_quartos.adicionar_quartos('casal', 5)
# gestao_quartos.adicionar_quartos('compartilhado', 10)
