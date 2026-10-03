import pandas as pd
import matplotlib.pyplot as plt
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from conexao import conectar


conexao = conectar()

consulta = """
SELECT
    YEAR(DataVenda) AS Ano,
    MONTH(DataVenda) AS Mes,
    AVG(ValorTotal) AS TicketMedio
FROM Vendas
GROUP BY YEAR(DataVenda), MONTH(DataVenda)
ORDER BY Ano, Mes;
"""

df = pd.read_sql(consulta, conexao)

conexao.close()


meses = {
    1: "Janeiro",
    2: "Fevereiro",
    3: "Março",
    4: "Abril",
    5: "Maio",
    6: "Junho",
    7: "Julho",
    8: "Agosto",
    9: "Setembro",
    10: "Outubro",
    11: "Novembro",
    12: "Dezembro"
}

df["Periodo"] = df["Mes"].map(meses)


plt.figure(figsize=(10, 6))

plt.bar(df["Periodo"], df["TicketMedio"])

plt.title("Ticket Médio Mensal")
plt.xlabel("Mês")
plt.ylabel("Ticket Médio (R$)")


for i, valor in enumerate(df["TicketMedio"]):
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