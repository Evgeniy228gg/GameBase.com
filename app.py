from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

# Функция для подключения к базе данных
def get_db_connection():
    conn = sqlite3.connect('templates/mydatabase.db')  # Имя базы данных
    conn.row_factory = sqlite3.Row  # Позволяет обращаться к данным как к словарям
    return conn

# Главная страница, отображающая список пользователей
@app.route('/')
def index():
    conn = get_db_connection()  # Подключаемся к базе данных
    cursor = conn.cursor()

    # Получаем все записи из таблицы users
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()  # Извлекаем все строки

    conn.close()  # Закрываем соединение

    # Передаем данные в шаблон (HTML)
    return render_template('index.html', users=users)

if __name__ == '__main__':
    app.run(debug=True)
