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

    def excluir_quarto(self, numero):
            for quarto in self.quartos:
                if quarto.numero == numero:
                    self.quartos.remove(quarto)
                    return True
            return False

# Exemplo de uso:
# gestao_quartos = GestaoQuartos()
# gestao_quartos.adicionar_quartos('casal', 5)
# gestao_quartos.adicionar_quartos('compartilhado', 10)
# print(gestao_quartos.excluir_quarto(3))  # True se o quarto foi excluído, False se não foi encontrado
