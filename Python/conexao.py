import pyodbc


def conectar():
    servidor = "localhost"
    banco = "Taskmaster"

    conexao = pyodbc.connect(
        f"DRIVER={{ODBC Driver 17 for SQL Server}};"
        f"SERVER={servidor};"
        f"DATABASE={banco};"
        "Trusted_Connection=yes;"
        "TrustServerCertificate=yes;"
    )

    return conexao