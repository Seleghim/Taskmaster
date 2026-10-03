import pandas as pd
from conexao import conectar

# ==============================
# CONEXÃO COM O BANCO
# ==============================

conexao = conectar()

# ==============================
# CONSULTA DAS VENDAS
# ==============================

consulta = """
SELECT
    V.VendaID,
    C.Nome AS Cliente,
    V.DataVenda,
    V.ValorTotal
FROM Vendas V
INNER JOIN Clientes C
    ON V.ClienteID = C.ClienteID;
"""

df_vendas = pd.read_sql(consulta, conexao)

# ==============================
# INDICADORES
# ==============================

faturamento = df_vendas["ValorTotal"].sum()
quantidade_vendas = df_vendas["VendaID"].nunique()
ticket_medio = df_vendas["ValorTotal"].mean()

# ==============================
# RESULTADOS
# ==============================

print("\n========== ANÁLISE DE VENDAS ==========")

print(f"Faturamento total: R$ {faturamento:,.2f}")
print(f"Quantidade de vendas: {quantidade_vendas}")
print(f"Ticket médio: R$ {ticket_medio:,.2f}")

print("\n========================================")


# ==============================
# PRODUTOS MAIS VENDIDOS
# ==============================

consulta_produtos = """
SELECT
    P.NomeProduto,
    SUM(I.Quantidade) AS QuantidadeVendida
FROM ItensVenda I
INNER JOIN Produtos P
    ON I.ProdutoID = P.ProdutoID
GROUP BY P.NomeProduto
ORDER BY QuantidadeVendida DESC;
"""

df_produtos = pd.read_sql(consulta_produtos, conexao)

print("\n========== PRODUTOS MAIS VENDIDOS ==========")
print(df_produtos)
print("============================================")


# ==============================
# FATURAMENTO POR PRODUTO
# ==============================

consulta_faturamento_produtos = """
SELECT
    P.NomeProduto,
    SUM(I.Quantidade * I.PrecoUnitario) AS Faturamento
FROM ItensVenda I
INNER JOIN Produtos P
    ON I.ProdutoID = P.ProdutoID
GROUP BY P.NomeProduto
ORDER BY Faturamento DESC;
"""

df_faturamento_produtos = pd.read_sql(
    consulta_faturamento_produtos,
    conexao
)

print("\n========== FATURAMENTO POR PRODUTO ==========")
print(df_faturamento_produtos)
print("=============================================")
conexao.close()