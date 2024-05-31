class Relatorios:
    def __init__(self, gestao_quartos, gestao_auditorios, gestao_estadias):
        self.gestao_quartos = gestao_quartos
        self.gestao_auditorios = gestao_auditorios
        self.gestao_estadias = gestao_estadias

    def relatorio_quartos(self):
        for quarto in self.gestao_quartos.listar_quartos():
            status = "Reservado" if quarto.reservado else "Disponível"
            print(f"Quarto {quarto.numero}: {quarto.tipo} - {status} (Hospede: {quarto.hospede})")

    def relatorio_auditorios(self):
        for auditorio in self.gestao_auditorios.listar_auditorios():
            status = "Reservado" if auditorio.reservado else "Disponível"
            print(f"Auditorio {auditorio.numero}: Capacidade {auditorio.capacidade} - {status} (Hospede: {auditorio.hospede})")

    def relatorio_estadias_encerradas(self):
        valor_total = 0
        for estadia in self.gestao_estadias.estadias:
            if not estadia.quarto.reservado: # Assumindo que reservada = False significa que estadia foi encerrada
                print(f"Hospede: {estadia.nome_hospede}, Valor Total: {estadia.valor_total}")
                valor_total += estadia.valor_total
        print(f"Valor total de todas as estadias encerradas: {valor_total}")

# Exemplo de uso:
# relatorios = Relatorios(gestao_quartos, gestao_auditorios, gestao_estadias)
# relatorios.relatorio_quartos()
# relatorios.relatorio_auditorios()
# relatorios.relatorio_estadias_encerradas()
