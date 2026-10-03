# Taskmaster

## Projeto de Análise de Vendas e Estoque

O Taskmaster é um projeto que desenvolvi para colocar em prática meus conhecimentos de banco de dados, Python e análise de dados.

A ideia foi criar uma pequena base de dados de uma empresa fictícia, contendo informações de clientes, produtos, vendas e estoque. A partir desses dados, desenvolvi consultas em SQL e scripts em Python para gerar análises e visualizações.

Durante o projeto, trabalhei principalmente com **SQL Server, Python, Pandas e Matplotlib**, explorando informações como faturamento, vendas por produto, desempenho dos clientes e situação do estoque.

O projeto também faz parte do meu processo de aprendizado e construção de um portfólio na área de **Dados**.

## Tecnologias utilizadas

- **SQL Server** — armazenamento e gerenciamento do banco de dados.
- **Python** — desenvolvimento dos scripts de análise.
- **Pandas** — tratamento e análise dos dados.
- **Matplotlib** — criação dos gráficos e visualizações.
- **PyODBC** — conexão entre Python e SQL Server.
- **VS Code** — desenvolvimento e organização do projeto.

## Análises realizadas

Durante o desenvolvimento do projeto, foram criadas análises relacionadas a vendas, clientes, produtos e estoque:

- Faturamento total
- Quantidade de vendas
- Ticket médio
- Produtos mais vendidos
- Faturamento por produto
- Faturamento mensal
- Ticket médio mensal
- Faturamento por cliente
- Participação dos clientes no faturamento
- Estoque atual por produto
- Produtos abaixo do estoque mínimo
- Quantidade necessária para reposição de estoque

## Estrutura do projeto

```text
Taskmaster
│
├── Python
│   ├── conexao.py
│   ├── analise.py
│   ├── analise_clientes.py
│   ├── ver_clientes.py
│   ├── ver_produtos.py
│   │
│   └── graficos
│       ├── faturamento_produto.py
│       ├── faturamento_mensal.py
│       ├── quantidade_produtos.py
│       ├── ticket_medio_mensal.py
│       ├── faturamento_cliente.py
│       ├── participacao_clientes.py
│       ├── estoque_atual.py
│       └── estoque_baixo.py
│
├── README.md
└── .gitignore
