from conexao import conectar

c = conectar()
cur = c.cursor()

cur.execute("""
SELECT TABLE_NAME
FROM INFORMATION_SCHEMA.TABLES
WHERE TABLE_TYPE = 'BASE TABLE'
ORDER BY TABLE_NAME
""")

print([r[0] for r in cur.fetchall()])

c.close()