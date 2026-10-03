import pandas as pd
from conexao import conectar


# ==============================
# CONEXÃO COM O BANCO
# ==============================

conexao = conectar()


# ==============================
# ANÁLISE DOS CLIENTES
# ==============================

consulta = """
SELECT
    c.Nome AS Cliente,
    COUNT(v.VendaID) AS QuantidadeCompras,
    SUM(v.ValorTotal) AS FaturamentoTotal,
    AVG(v.ValorTotal) AS TicketMedio
FROM Vendas v
INNER JOIN Clientes c
    ON v.ClienteID = c.ClienteID
GROUP BY c.Nome
ORDER BY FaturamentoTotal DESC;
"""


df_clientes = pd.read_sql(consulta, conexao)

conexao.close()


# ==============================
# CLASSIFICAÇÃO DOS CLIENTES
# ==============================

df_clientes["TipoCliente"] = df_clientes["QuantidadeCompras"].apply(
    lambda x: "Cliente recorrente" if x >= 2 else "Cliente ocasional"
)
faturamento_total = df_clientes["FaturamentoTotal"].sum()

df_clientes["ParticipacaoFaturamento"] = (
    df_clientes["FaturamentoTotal"] / faturamento_total * 100
)

df_clientes["ParticipacaoFaturamento"] = df_clientes[
    "ParticipacaoFaturamento"
].round(2)

# ==============================
# RESULTADOS
# ==============================

print("\n========== ANÁLISE DE CLIENTES ==========")

print(df_clientes.to_string(index=False))

print("\n==========================================")