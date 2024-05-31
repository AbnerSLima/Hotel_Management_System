class Auditorio:
    def __init__(self, numero, capacidade):
        self.numero = numero
        self.capacidade = capacidade
        self.reservado = False
        self.hospede = None

class GestaoAuditorios:
    def __init__(self):
        self.auditorios = []

    def adicionar_auditorios(self, capacidade, quantidade):
        numero_inicial = len(self.auditorios) + 1
        for i in range(quantidade):
            self.auditorios.append(Auditorio(numero_inicial + i, capacidade))

    def listar_auditorios(self):
        return self.auditorios

    def buscar_auditorios_disponiveis(self):
        return [auditorio for auditorio in self.auditorios if not auditorio.reservado]

# Exemplo de uso:
# gestao_auditorios = GestaoAuditorios()
# gestao_auditorios.adicionar_auditorios(30, 2)
# gestao_auditorios.adicionar_auditorios(10, 3)
