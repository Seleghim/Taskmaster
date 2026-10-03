import pandas as pd
import matplotlib.pyplot as plt
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from conexao import conectar


conexao = conectar()

consulta = """
SELECT
    c.Nome,
    SUM(v.ValorTotal) AS Faturamento
FROM Vendas v
INNER JOIN Clientes c
    ON v.ClienteID = c.ClienteID
GROUP BY c.Nome
ORDER BY Faturamento DESC;
"""

df = pd.read_sql(consulta, conexao)


conexao.close()


plt.figure(figsize=(10, 6))

plt.bar(df["Nome"], df["Faturamento"])

plt.title("Faturamento por Cliente")
plt.xlabel("Cliente")
plt.ylabel("Faturamento (R$)")

plt.xticks(rotation=45, ha="right")


for i, valor in enumerate(df["Faturamento"]):
    valor_formatado = (
        f"R$ {valor:,.2f}"
        .replace(",", "X")
        .replace(".", ",")
        .replace("X", ".")
    )

    plt.text(
        i,
        valor,
        valor_formatado,
        ha="center",
        va="bottom"
    )


plt.tight_layout()
plt.show()