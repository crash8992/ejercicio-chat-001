from dataBase import conn

cursor = conn.cursor
cursor.execute('SELECT * FROM users')

for row in cursor:
    print(row)
    
conn.close

