import sqlite3

connect = sqlite3.connect('cars.db')
cursor = connect.cursor()
# cursor.execute('INSERT INTO parking (price, model) VALUES (14444, "Tesla")')
# connect.commit()


id_ = input()

#cursor.execute(f'SELECT * FROM parking WHERE id=?', (id_,))
cursor.execute('SELECT * FROM parking')
# for data in cursor.fetchmany(2):
#     print(data)

while cursor:
    result = cursor.fetchmany(2)
    if not result:
        break

    print(result)
cursor.close()
