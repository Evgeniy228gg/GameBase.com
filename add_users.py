import sqlite3

# Подключаемся к базе данных (если ее нет, она будет создана)
conn = sqlite3.connect('templates/mydatabase.db')
cursor = conn.cursor()

# Создаем таблицу users, если ее нет
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        email TEXT NOT NULL
    )
''')

# Добавляем пользователей
cursor.execute("INSERT INTO users (username, email) VALUES (?, ?)", ('JohnDoe', 'john@example.com'))
cursor.execute("INSERT INTO users (username, email) VALUES (?, ?)", ('JaneSmith', 'jane@example.com'))

# Сохраняем изменения
conn.commit()

# Закрываем соединение
conn.close()

print("Пользователи успешно добавлены!")
