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
    e.QuantidadeAtual,
    e.EstoqueMinimo,
    e.EstoqueMinimo - e.QuantidadeAtual AS QuantidadeRepor
FROM Estoque e
INNER JOIN Produtos p
    ON e.ProdutoID = p.ProdutoID
WHERE e.QuantidadeAtual < e.EstoqueMinimo
ORDER BY QuantidadeRepor DESC;
"""

df = pd.read_sql(consulta, conexao)

conexao.close()


plt.figure(figsize=(10, 6))

plt.bar(
    df["NomeProduto"],
    df["QuantidadeRepor"]
)

plt.title("Produtos que Precisam de Reposição")
plt.xlabel("Produto")
plt.ylabel("Quantidade a Repor")

plt.xticks(rotation=45, ha="right")


for i, valor in enumerate(df["QuantidadeRepor"]):
    plt.text(
        i,
        valor,
        str(valor),
        ha="center",
        va="bottom"
    )


plt.tight_layout()
plt.show()