import sqlite3
conn = sqlite3.connect("Contatos.db")

cursor = conn.cursor()


create_table = ("""
CREATE TABLE IF NOT EXISTS Contatos (
    id INTEGER PRIMARY KEY,
    nome TEXT NOT NULL,
    email TEXT NOT NULL,
    numero INTEGER NOT NULL
    )
""")
conn.execute(create_table)

conn.commit()

adicionar_contato = ("Marko","Marko@gmal,com",629345678)
contato = ("INSERT INTO Contatos (nome,email,numero) VALUES (?,?,?)")
cursor.execute(contato,adicionar_contato)
#contato_id = 3
# novo_nome = ("Ramon")
# atualizar_contato = ("UPDATE Contatos SET nome = ? WHERE id = ? ")
# cursor.execute(atualizar_contato,(novo_nome,contato_id))
# conn.commit()



    
