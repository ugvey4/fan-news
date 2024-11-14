import sqlite3 as sql

def create_data_base():
    conn = sql.connect('fan.db')
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL
        )
    ''')
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS teams (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            team_name TEXT NOT NULL,
            user_id INTEGER,
            FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
        )
    ''')
    
    conn.commit()
    conn.close()

def add_user(username, password):
    conn = sql.connect('fan.db')
    cursor = conn.cursor()
    
    cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
    conn.commit()
    conn.close()

def check_username(username):
    conn = sql.connect('fan.db')
    cursor = conn.cursor()
    
    cursor.execute("SELECT 1 FROM users WHERE username = ?", (username))
    result = cursor.fetchone()
    
    conn.close()
    return result is not None

def check_password(username):
    conn = sql.connect('fan.db')
    cursor = conn.cursor()
    
    cursor.execute("SELECT password FROM users WHERE username = ?", (username))
    result = cursor.fetchone()
    conn.close()
    
    if result is None:
        return None
    return result[0]

def add_team(user_id, team_name):
    conn = sql.connect('fan.db')
    cursor = conn.cursor()
    
    cursor.execute('INSERT INTO teams (team_name, user_id) VALUES (?, ?)', (team_name, user_id))
    conn.commit()
    conn.close()

def get_teams_by_user(user_id):
    conn = sql.connect('fan.db')
    cursor = conn.cursor()
    
    cursor.execute("SELECT team_name FROM teams WHERE user_id = ?", (user_id,))
    results = cursor.fetchall()
    conn.close()
    
    return results

if __name__ == '__main__':
    create_data_base()
