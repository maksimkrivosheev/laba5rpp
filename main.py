import sqlite3


# Раздел I. Работа с базой данных Sqlite.

# 1. Создание таблицы «users» через консоль
def create_users_table():
    conn = sqlite3.connect('Userss.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY,
                    name TEXT,
                    email TEXT
                )''')
    conn.commit()
    conn.close()


# 2. Добавление нового пользователя через консоль
def add_user(name, email):
    conn = sqlite3.connect('Userss.db')
    c = conn.cursor()
    c.execute("INSERT INTO users (name, email) VALUES (?, ?)", (name, email))
    conn.commit()
    conn.close()


# 3. Получение всех пользователей из таблицы «users» через консоль
def get_all_users():
    conn = sqlite3.connect('Userss.db')
    c = conn.cursor()
    c.execute("SELECT * FROM users")
    users = c.fetchall()
    conn.close()
    return users


# 4. Получение пользователя по id из таблицы «users» через консоль
def get_user_by_id(user_id):
    conn = sqlite3.connect('Userss.db')
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE id = ?", (user_id,))
    user = c.fetchone()
    conn.close()
    return user


# 5. Удаление пользователя по id из таблицы «users» через консоль
def delete_user_by_id(user_id):
    conn = sqlite3.connect('Userss.db')
    c = conn.cursor()
    c.execute("DELETE FROM users WHERE id = ?", (user_id,))
    conn.commit()
    conn.close()


# Раздел II. Тестирование приложения

# 1. Функция main
def main():
    create_users_table()

    # Добавление нового пользователя через консоль
    name = input("Введите имя пользователя: ")
    email = input("Введите email пользователя: ")
    add_user(name, email)

    # Получение всех пользователей
    print("Все пользователи:")
    all_users = get_all_users()
    for user in all_users:
        print(user)

    # Получение пользователя по id
    user_id = int(input("Введите id пользователя для поиска: "))
    user = get_user_by_id(user_id)
    if user:
        print("Пользователь с id", user_id, ":", user)
    else:
        print("Пользователь не найден.")

    # Удаление пользователя по id
    user_id = int(input("Введите id пользователя для удаления: "))
    delete_user_by_id(user_id)
    print("Пользователь с id", user_id, "удален.")


if __name__ == "__main__":
    main()
