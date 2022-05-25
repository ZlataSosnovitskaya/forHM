import sqlite3 as dbms

db=dbms.connect('dub.db')

cursor=db.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS users (
    login TEXT, 
    password TEXT
)""")
db.commit()

user_login = input('login:  ')
user_password = input('password:  ')

cursor.execute("SELECT * FROM users WHERE login=?", (user_login,))

if cursor.fetchone() is None:
    cursor.execute("INSERT INTO users VALUES(? ,?)",(user_login,user_password))
    db.commit()
    print('Регистрация окончена')
    cursor.execute("SELECT * FROM users")
    print(cursor.fetchall())
else:
    print('Такая запись уже существует')
    for value in cursor.execute("SELECT * FROM users"):
        print(value)
db.close()
