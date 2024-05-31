class GestaoRefeicoes:
    def __init__(self):
        self.refeicoes = {}

    def adicionar_refeicao(self, hospede, tipo_refeicao):
        if hospede not in self.refeicoes:
            self.refeicoes[hospede] = []
        self.refeicoes[hospede].append(tipo_refeicao)

# Exemplo de uso:
# gestao_refeicoes = GestaoRefeicoes()
# gestao_refeicoes.adicionar_refeicao('João', 'Café da manhã')
