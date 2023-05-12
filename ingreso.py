from dataBase import conn

cursor = conn.cursor()
cursor.execute('CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)')

name = input("INGRESE NOMBRE A GUARDAR: ")
age = int(input("INGRESE LA EDAD DEL USUARIO"))

cursor.execute('INSERT INTO users (name, age) VALUES (?, ?)', (name, age))
conn.commit()

conn.close()