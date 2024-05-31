# Hotel_Management_System

Um sistema de gestão de hotel genérico desenvolvido em Python. Este projeto visa atender à maioria das propostas de hospedagem, permitindo a gestão de quartos, auditórios, estadias e refeições.

## Funcionalidades

- **Gestão de Quartos**: Adicionar e listar quartos disponíveis, buscando quartos disponíveis para reservas.
- **Gestão de Auditórios**: Adicionar e listar auditórios/salas de reunião, buscando auditórios disponíveis para reservas.
- **Gestão de Refeições**: Adicionar refeições durante a estadia do cliente.
- **Gestão de Estadias**: Cadastrar estadias de hóspedes, incluindo reservas de quartos, refeições e auditórios.
- **Relatórios**: Gerar relatórios de quartos, auditórios e estadias encerradas.
- **Check-in e Check-out**: Gerenciar check-in e check-out de hóspedes.

## Estrutura do Projeto

```plaintext
Hotel_Management_System/
│
├── gestao_quartos.py       # Gerencia a adição e listagem de quartos.
├── gestao_auditorios.py    # Gerencia a adição e listagem de auditórios.
├── gestao_refeicoes.py     # Gerencia as refeições dos hóspedes.
├── gestao_estadias.py      # Gerencia o cadastro e manutenção de estadias.
├── relatorios.py           # Gera relatórios de quartos, auditórios e estadias encerradas.
├── sistema_gestao_hotel.py # Ponto de entrada principal do sistema com menu e navegação.
├── README.md
└── .gitignore
