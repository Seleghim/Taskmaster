import pandas as pd
import matplotlib.pyplot as plt
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from conexao import conectar


conexao = conectar()

consulta = """
SELECT
    c.Nome AS Cliente,
    SUM(v.ValorTotal) AS Faturamento
FROM Vendas v
INNER JOIN Clientes c
    ON v.ClienteID = c.ClienteID
GROUP BY c.Nome
ORDER BY Faturamento DESC;
"""

df = pd.read_sql(consulta, conexao)

conexao.close()


faturamento_total = df["Faturamento"].sum()

df["Participacao"] = (
    df["Faturamento"] / faturamento_total * 100
)


plt.figure(figsize=(10, 6))

plt.bar(
    df["Cliente"],
    df["Participacao"]
)

plt.title("Participação dos Clientes no Faturamento")
plt.xlabel("Cliente")
plt.ylabel("Participação (%)")

plt.xticks(rotation=45, ha="right")


for i, valor in enumerate(df["Participacao"]):
    plt.text(
        i,
        valor,
        f"{valor:.2f}%",
        ha="center",
        va="bottom"
    )


plt.tight_layout()
plt.show()