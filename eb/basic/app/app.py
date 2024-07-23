from flask import Flask
import psycopg2

app = Flask(__name__)

# Function to connect to the database
def get_db_connection():
    conn = psycopg2.connect(database="", user="postgres", password="password", host="localhost", port="5432")
    return conn

@app.route("/")
def hello_world():
    conn = get_db_connection()

    cursor = conn.cursor()

    cursor.execute('SELECT * FROM users')
    data = cursor.fetchall()

    cursor.close()
    conn.close()

    return data

@app.route('/create_table')
def create_table():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            name VARCHAR(50) NOT NULL,
            age INTEGER NOT NULL
        )
    ''')
    conn.commit()
    cur.close()
    conn.close()
    
    return 'Table created!'

@app.route('/add_user')
def add_user():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('''
        INSERT INTO users (name, age)
        VALUES (%s, %s)
    ''', ('Emmanuel', 19))
    conn.commit()
    cur.close()
    conn.close()

    return 'User added!'

if __name__ == '__main__':
    app.run(debug=True)