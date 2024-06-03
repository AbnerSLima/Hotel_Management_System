import os
import sys

from gestao_quartos import GestaoQuartos
from gestao_auditorios import GestaoAuditorios
from gestao_refeicoes import GestaoRefeicoes
from gestao_estadias import GestaoEstadias
from relatorios import Relatorios

def limpar():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

class SistemaGestaoHotel:
    def __init__(self):
        self.gestao_quartos = GestaoQuartos()
        self.gestao_auditorios = GestaoAuditorios()
        self.gestao_refeicoes = GestaoRefeicoes()
        self.gestao_estadias = GestaoEstadias(self.gestao_quartos, self.gestao_auditorios, self.gestao_refeicoes)
        self.relatorios = Relatorios(self.gestao_quartos, self.gestao_auditorios, self.gestao_estadias)

    def login(self):
        while True:
            limpar()
            print("- - - USUÁRIO - - -")
            print("1. Gerente")
            print("2. Operário")
            print("3. Encerrar")
            opcao = input("Escolha uma opção: ")

            if opcao == '1':
                self.menu1()
            elif opcao == '2':
                self.menu2()
            elif opcao == '3':
                sys.exit()
            else:
                print("Opção inválida. Tente novamente.")

    def menu1(self):
        while True:
            limpar()
            print("- - - - MEMU - - - -")
            print("1. Cadastros")
            print("2. Checkin")
            print("3. Checkout")
            print("4. Relatórios")
            print("5. Encerrar")
            opcao = input("Escolha uma opção: ")

            if opcao == '1':
                self.cadastro()
            elif opcao == '2':
                if self.gestao_quartos.quartos:
                    self.checkin()
                else:
                    print("Não há quartos cadastrados. Por favor, cadastre um quarto primeiro.")
                    input("\nAperte Enter para retornar ao Menu Principal")
            elif opcao == '3':
                self.checkout()
            elif opcao == '4':
                self.relatorios_menu()
            elif opcao == '5':
                sys.exit()
            else:
                print("Opção inválida. Tente novamente.")

    def menu2(self):
        while True:
            limpar()
            print("- - - - MEMU - - - -")
            print("1. Checkin")
            print("2. Checkout")
            print("3. Relatórios")
            print("4. Encerrar")
            opcao = input("Escolha uma opção: ")

            if opcao == '1':
                if self.gestao_quartos.quartos:
                    self.checkin()
                else:
                    print("Não há quartos cadastrados. Por favor, cadastre um quarto primeiro.")
                    input("\nAperte Enter para retornar ao Menu Principal")
            elif opcao == '2':
                self.checkout()
            elif opcao == '3':
                self.relatorios_menu()
            elif opcao == '4':
                sys.exit()
            else:
                print("Opção inválida. Tente novamente.")

    def cadastro(self):
        limpar()
        print("- - - - Cadastro - - - -")
        print("1. Cadastrar quarto")
        print("2. Cadastrar auditório")
        print("3. Excluir quarto")
        print("4. Excluir auditório")
        print("5. Retornar ao Menu Principal")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            limpar()
            print("- - - Cadastro de quarto - - -")
            tipo = input("\nTipo de quarto: ")
            quantidade = int(input("Quantidade: "))
            self.gestao_quartos.adicionar_quartos(tipo, quantidade)

        elif opcao == '2':
            capacidade = int(input("Capacidade do auditório: "))
            quantidade = int(input("Quantidade: "))
            self.gestao_auditorios.adicionar_auditorios(capacidade, quantidade)

        elif opcao == '3':
            limpar()
            if self.gestao_quartos.quartos:
                self.relatorios.relatorio_quartos()
                numero = int(input("\nNúmero do quarto a ser excluído: "))
                if self.gestao_quartos.excluir_quarto(numero):
                    print(f"\nQuarto {numero} excluído com sucesso.")
                else:
                    print(f"\nQuarto {numero} não encontrado.")
                input("\nAperte Enter para retornar ao Menu Principal")
            else:
                print("Não há quartos cadastrados. Por favor, cadastre um quarto primeiro.")
                input("\nAperte Enter para retornar ao Menu Principal")

        elif opcao == '4':
            limpar()
            if self.gestao_auditorios.auditorios:
                self.relatorios.relatorio_auditorios()
                numero = int(input("\nNúmero do auditório a ser excluído: "))
                if self.gestao_auditorios.excluir_auditorio(numero):
                    print(f"\nAuditório {numero} excluído com sucesso.")
                else:
                    print(f"\nAuditório {numero} não encontrado.")
                input("\nAperte Enter para retornar ao Menu Principal")
            else:
                print("Não há auditórios cadastrados. Por favor, cadastre um auditório primeiro.")
                input("\nAperte Enter para retornar ao Menu Principal")

        elif opcao == '5':
            limpar()
        else:
            print("Opção inválida.")

    def checkin(self):
        limpar()
        print("- - - - Checkin - - - - ")

        print("- - - Lista de quartos - - -")
        self.relatorios.relatorio_quartos()
        nome_hospede = input("\nNome do hospede: ")
        quartos_disponiveis = self.gestao_quartos.buscar_quartos_disponiveis()
        for quarto in quartos_disponiveis:
            print(f"Quarto {quarto.numero}: {quarto.tipo}")
        numero_quarto = int(input("Numero do quarto: "))
        camas = int(input("Quantidade de camas: "))
        valor_camas = float(input("Valor total das camas: "))
        refeicao = input("Deseja refeição durante a estadia? (s/n): ")
        valor_refeicao = 0
        tipo_refeicao = None
        if refeicao.lower() == 's':
            tipo_refeicao = input("Tipo de refeição: ")
            valor_refeicao = float(input("Valor total da refeição: "))
            self.gestao_refeicoes.adicionar_refeicao(nome_hospede, tipo_refeicao)
        auditorio = input("Deseja reserva de auditório? (s/n): ")
        valor_auditorio = 0
        numero_auditorio = None
        if auditorio.lower() == 's':
            auditorios_disponiveis = self.gestao_auditorios.buscar_auditorios_disponiveis()
            for aud in auditorios_disponiveis:
                print(f"Auditório {aud.numero}: Capacidade {aud.capacidade}")
            numero_auditorio = int(input("Número do auditório: "))
            valor_auditorio = float(input("Valor total do auditório: "))
        self.gestao_estadias.cadastrar_estadia(nome_hospede, numero_quarto, camas, valor_camas, tipo_refeicao, valor_refeicao, numero_auditorio, valor_auditorio)        
        input("\nAperte Enter para retornar ao Menu Principal")

    def checkout(self):
        limpar()
        print("- - - - Checkout - - - -")
        nome_hospede = input("Nome do hospede para checkout: ")
        for estadia in self.gestao_estadias.estadias:
            if estadia.nome_hospede == nome_hospede and estadia.quarto.reservado:
                estadia.quarto.reservado = False
                if estadia.auditorio:
                    estadia.auditorio.reservado = False
                print(f"Nome: {estadia.nome_hospede}")
                print(f"Quarto: {estadia.quarto.numero} - {estadia.quarto.tipo}")
                print(f"Camas: {estadia.camas} - Valor: {estadia.valor_camas}")
                if estadia.refeicao:
                    print(f"Refeição: {estadia.refeicao} - Valor: {estadia.valor_refeicao}")
                if estadia.auditorio:
                    print(f"Auditório: {estadia.auditorio.numero} - Valor: {estadia.valor_auditorio}")
                print(f"Valor Total: {estadia.valor_total}")
                faturar = input("Deseja faturar? (s/n): ")
                if faturar.lower() == 's':
                    forma_pagamento = input("Forma de pagamento: ")
                    print(f"Recibo: Nome: {estadia.nome_hospede}, Valor Total: {estadia.valor_total}, Forma de pagamento: {forma_pagamento}")
                    print("Checkout realizado com sucesso.")
                    input("\nAperte Enter para retornar ao Menu Principal")
                else:
                    estadia.quarto.reservado = True
                    if estadia.auditorio:
                        estadia.auditorio.reservado = True

    def relatorios_menu(self):
        limpar()
        print("- - - - Relatórios - - - -")
        print("1. Relatório de quartos")
        print("2. Relatório de auditórios")
        print("3. Relatório de estadias encerradas")
        print("4. Retornar ao Menu Principal")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            limpar()
            print("- - - - Relatório de quartos - - - -")
            self.relatorios.relatorio_quartos()
            input("\nAperte Enter para retornar ao Menu Principal")
        elif opcao == '2':
            limpar()
            print("- - - - Relatório de auditórios - - - -")
            self.relatorios.relatorio_auditorios()
            input("\nAperte Enter para retornar ao Menu Principal")
        elif opcao == '3':
            limpar()
            print("- - - - Relatório de estadias encerradas - - - -")
            self.relatorios.relatorio_estadias_encerradas()
            input("\nAperte Enter para retornar ao Menu Principal")
        elif opcao == '4':
            limpar()
        else:
            limpar()
            print("- - - - Relatórios - - - -")
            print("Opção inválida.")
            input("\nAperte Enter para retornar ao Menu Principal")

if __name__ == "__main__":
    sistema = SistemaGestaoHotel()
    sistema.login()