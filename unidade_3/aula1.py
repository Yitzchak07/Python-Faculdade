import sqlite3
from time import sleep

conn = sqlite3.connect("exemplo.db")

cursor = conn.cursor()

create_table = ("""

CREATE TABLE IF NOT EXISTS Produtos (
    id INTEGER PRIMARY KEY,
    nome TEXT NOT NULL,
    preco REAL NOT NULL,
    estoque INTEGER
    )
""")

cursor.execute(create_table)
conn.commit()
sleep(1)

nov_porduto = ("Tenis",250.00,20)

inserir_produto = ("INSERT INTO Produtos (nome,preco,estoque) VALUES (?,?,?)")

cursor.execute(inserir_produto, nov_porduto)
conn.commit()
sleep(1)

selecionar_produto = ("SELECT * FROM Produtos")

cursor.execute(selecionar_produto)
produtos = cursor.fetchall()
for produto in produtos:
     print(produto)
sleep(1)

novo_preco = 30.99
produto_id = 1
atualizar_preco = ("UPDATE Produtos SET preco = ? WHERE id = ?")
cursor.execute(atualizar_preco,(novo_preco,produto_id))
conn.commit()

sleep(1)

produto_id = 1
excluir_produto = ("DELETE FROM Produtos WHERE id - ?")
cursor.execute(excluir_produto, (produto_id,))
conn.commit()
conn.close()
