# Desafio 3 - Sistema de Agendamento de Consultas em Unidade Básica de Saúde

## 🎯 Objetivo do Sistema

Este projeto é um sistema de gerenciamento para uma Unidade Básica de Saúde, desenvolvido em Python com uso em terminal. Ele resolve o problema da organização e registro de informações essenciais, permitindo o controle de cadastros de médicos, pacientes e o agendamento de consultas.

O sistema é destinado a usuários administrativos da clínica (como recepcionistas ou gestores), facilitando o acesso, a manipulação e a geração de relatórios simples sobre os dados da operação.

## ⚙️ Funcionalidades Principais

O sistema é dividido em quatro módulos principais, além de um sistema de persistência de dados:

* **Módulo Médicos (CRUD)**
    * Cadastrar novo médico (com validação de CRM).
    * Visualizar informações de um médico específico (busca por CRM).
    * Alterar dados cadastrais de um médico.
    * Excluir um médico do sistema.

* **Módulo Pacientes (CRUD)**
    * Cadastrar novo paciente (com validação de CPF).
    * Visualizar informações de um paciente específico (busca por CPF).
    * Alterar dados cadastrais de um paciente.
    * Excluir um paciente do sistema.

* **Módulo Consultas (CRUD)**
    * Agendar uma nova consulta (vinculando um médico e um paciente já cadastrados).
    * Visualizar detalhes de uma consulta específica (busca por ID).
    * Alterar dados de uma consulta (médico, paciente, queixa, data).
    * Excluir/Cancelar uma consulta agendada.

* **Módulo Relatórios**
    * Gerar um relatório que lista todos os médicos e a quantidade de consultas agendadas para cada um.
    * Gerar um relatório que agrupa a quantidade de consultas por data.

* **Persistência de Dados**
    * Todas as informações de médicos, pacientes e consultas são salvas localmente em arquivos `.json` (dentro de um diretório `dados/`), garantindo que os dados não sejam perdidos ao fechar o programa.

## 🚀 Instruções de Execução

1.  Clone este repositório ou faça o download dos arquivos do projeto.

2.  Certifique-se de que você tem o **Python 3.10** (ou superior) instalado.
    > **Nota:** O projeto utiliza a estrutura `match-case`, introduzida no Python 3.10.

3.  Este projeto utiliza apenas bibliotecas padrão do Python (`json`, `os`, `re`, `datetime`), portanto, **não é necessário instalar dependências** externas.

4.  Abra seu terminal e navegue até a pasta raiz onde o arquivo `main.py` está localizado.

5.  Execute o programa com o seguinte comando:

    ```bash
    python main.py
    ```