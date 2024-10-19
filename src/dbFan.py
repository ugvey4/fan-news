import sqlite3 as sql

def create_data_base():
    conn = sql.connect('fan.db')
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            password TEXT NOT NULL,
            team TEXT,
            league TEXT
        )
    ''')
    
    conn.commit()
    conn.close()

def add_columns():
    conn = sql.connect('fan.db')
    cursor = conn.cursor()
    
    try:
        cursor.execute("ALTER TABLE users ADD COLUMN team TEXT;")
    except sql.OperationalError:
        pass
    try:
        cursor.execute("ALTER TABLE users ADD COLUMN league TEXT;")
    except sql.OperationalError:
        pass

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
    
    cursor.execute("SELECT 1 FROM users WHERE username = ?", (username,))
    result = cursor.fetchone()
    
    conn.close()
    return result is not None

def check_password(username):
    conn = sql.connect('fan.db')
    cursor = conn.cursor()
    
    cursor.execute("SELECT password FROM users WHERE username = ?", (username,))
    result = cursor.fetchone()
    conn.close()
    
    if result is None:
        return None
    return result[0]

def add_league(username, league):
    conn = sql.connect('fan.db')
    cursor = conn.cursor()
    
    cursor.execute('UPDATE users SET league = ? WHERE username = ?', (league, username))
    conn.commit()
    conn.close()

def add_teams(username, team_name):
    conn = sql.connect('fan.db')
    cursor = conn.cursor()
    
    cursor.execute('UPDATE users SET team = ? WHERE username = ?', (team_name, username))
    conn.commit()
    conn.close()

if __name__ == '__main__':
    create_data_base()