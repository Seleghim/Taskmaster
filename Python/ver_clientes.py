from conexao import conectar

c = conectar()
cur = c.cursor()

cur.execute("""
SELECT COLUMN_NAME
FROM INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_NAME = 'Clientes'
ORDER BY ORDINAL_POSITION
""")

print([r[0] for r in cur.fetchall()])

c.close()