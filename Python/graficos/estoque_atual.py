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
    e.QuantidadeAtual
FROM Estoque e
INNER JOIN Produtos p
    ON e.ProdutoID = p.ProdutoID
ORDER BY e.QuantidadeAtual DESC;
"""

df = pd.read_sql(consulta, conexao)

conexao.close()


plt.figure(figsize=(10, 6))

plt.bar(df["NomeProduto"], df["QuantidadeAtual"])

plt.title("Estoque Atual por Produto")
plt.xlabel("Produto")
plt.ylabel("Quantidade em Estoque")

plt.xticks(rotation=45, ha="right")


for i, valor in enumerate(df["QuantidadeAtual"]):
    plt.text(
        i,
        valor,
        str(valor),
        ha="center",
        va="bottom"
    )


plt.tight_layout()
plt.show()