from gestao_quartos import GestaoQuartos
from gestao_auditorios import GestaoAuditorios
from gestao_refeicoes import GestaoRefeicoes

class Estadia:
    def __init__(self, nome_hospede, quarto, camas, valor_camas, refeicao=None, valor_refeicao=0, auditorio=None, valor_auditorio=0):
        self.nome_hospede = nome_hospede
        self.quarto = quarto
        self.camas = camas
        self.valor_camas = valor_camas
        self.refeicao = refeicao
        self.valor_refeicao = valor_refeicao
        self.auditorio = auditorio
        self.valor_auditorio = valor_auditorio
        self.valor_total = valor_camas + valor_refeicao + valor_auditorio

class GestaoEstadias:
    def __init__(self, gestao_quartos, gestao_auditorios, gestao_refeicoes):
        self.gestao_quartos = gestao_quartos
        self.gestao_auditorios = gestao_auditorios
        self.gestao_refeicoes = gestao_refeicoes
        self.estadias = []

    def cadastrar_estadia(self, nome_hospede, numero_quarto, camas, valor_camas, refeicao=None, valor_refeicao=0, numero_auditorio=None, valor_auditorio=0):
        quarto = next((q for q in self.gestao_quartos.listar_quartos() if q.numero == numero_quarto), None)
        auditorio = next((a for a in self.gestao_auditorios.listar_auditorios() if a.numero == numero_auditorio), None)
        estadia = Estadia(nome_hospede, quarto, camas, valor_camas, refeicao, valor_refeicao, auditorio, valor_auditorio)
        self.estadias.append(estadia)
        if quarto:
            quarto.reservado = True
            quarto.hospede = nome_hospede
        if auditorio:
            auditorio.reservado = True
            auditorio.hospede = nome_hospede

# Exemplo de uso:
# gestao_quartos = GestaoQuartos()
# gestao_auditorios = GestaoAuditorios()
# gestao_refeicoes = GestaoRefeicoes()
# gestao_estadias = GestaoEstadias(gestao_quartos, gestao_auditorios, gestao_refeicoes)
# gestao_estadias.cadastrar_estadia('João', 1, 2, 200, 'Café da manhã', 50, 1, 100)
