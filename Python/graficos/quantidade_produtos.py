import pandas as pd
import matplotlib.pyplot as plt
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from conexao import conectar


conexao = conectar()

consulta = """
SELECT
    p.NomeProduto,
    SUM(iv.Quantidade) AS QuantidadeVendida
FROM ItensVenda iv
INNER JOIN Produtos p
    ON iv.ProdutoID = p.ProdutoID
GROUP BY p.NomeProduto
ORDER BY QuantidadeVendida DESC;
"""

df = pd.read_sql(consulta, conexao)

conexao.close()


plt.figure(figsize=(10, 6))

plt.bar(df["NomeProduto"], df["QuantidadeVendida"])

plt.title("Quantidade de Produtos Vendidos")
plt.xlabel("Produto")
plt.ylabel("Quantidade Vendida")

plt.xticks(rotation=45, ha="right")


for i, valor in enumerate(df["QuantidadeVendida"]):
    plt.text(
        i,
        valor,
        str(valor),
        ha="center",
        va="bottom"
    )


plt.tight_layout()
plt.show()