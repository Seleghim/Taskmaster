import pandas as pd
import matplotlib.pyplot as plt
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from conexao import conectar

# Conecta ao banco de dados
conexao = conectar()

# Consulta os dados de faturamento por produto
consulta = """
SELECT
    p.NomeProduto,
    SUM(iv.Quantidade * iv.PrecoUnitario) AS Faturamento
FROM ItensVenda iv
INNER JOIN Produtos p
    ON iv.ProdutoID = p.ProdutoID
GROUP BY p.NomeProduto
ORDER BY Faturamento DESC;
"""

# Executa a consulta
df = pd.read_sql(consulta, conexao)

# Fecha a conexão
conexao.close()

# Mostra os dados no terminal
print(df)

# Cria o gráfico
plt.figure(figsize=(10, 6))
plt.bar(df["NomeProduto"], df["Faturamento"])

plt.title("Faturamento por Produto")
plt.xlabel("Produto")
plt.ylabel("Faturamento (R$)")

plt.xticks(rotation=45, ha="right")

# Adiciona os valores sobre as colunas
for i, valor in enumerate(df["Faturamento"]):
    plt.text(i, valor, f"R$ {valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."), ha="center", va="bottom")
plt.tight_layout()

# Exibe o gráfico
plt.show()