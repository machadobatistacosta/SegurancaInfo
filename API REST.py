from flask import Flask, request, jsonify 
from werkzeug.security import generate_password_hash, check_password_hash 
from pyngrok import ngrok 
import sqlite3 
app = Flask(__name__) 
# Conectando ao banco de dados SQLite 
def init_db(): 
conn = sqlite3.connect('users.db') 
    c = conn.cursor() 
    c.execute(''' 
        CREATE TABLE IF NOT EXISTS users ( 
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            login TEXT NOT NULL UNIQUE, 
            password TEXT NOT NULL 
        ) 
    ''') 
    conn.commit() 
    conn.close() 
 
# Rota para a homepage 
@app.route('/') 
def home(): 
    return "API is running! Use /register to create a user and /login to 
authenticate." 
 
# Rota para criar usuários 
@app.route('/register', methods=['POST']) 
def register(): 
    data = request.get_json() 
    login = data.get('login') 
    password = data.get('password') 
 
    if not login or not password: 
        return jsonify({"message": "Login and password are required"}), 400 
 
    password_hash = generate_password_hash(password) 
 
    conn = sqlite3.connect('users.db') 
    c = conn.cursor() 
    try: 
        c.execute("INSERT INTO users (login, password) VALUES (?, ?)", (login, 
password_hash)) 
        conn.commit() 
        return jsonify({"message": "User created successfully"}), 201 
    except sqlite3.IntegrityError: 
        return jsonify({"message": "User already exists"}), 400 
    finally: 
        conn.close() 
 
# Rota para login 
@app.route('/login', methods=['POST']) 
def login(): 
    data = request.get_json() 
    login = data.get('login') 
    password = data.get('password') 
 
    if not login or not password: 
        return jsonify({"message": "Login and password are required"}), 400 
 
    conn = sqlite3.connect('users.db') 
    c = conn.cursor() 
    c.execute("SELECT password FROM users WHERE login = ?", (login,)) 
    row = c.fetchone() 
    conn.close() 
 
    if row and check_password_hash(row[0], password): 
        return jsonify({"message": "Login successful"}), 200 
    else: 
        return jsonify({"message": "Invalid login or password"}), 401 
 
# Inicializar o banco de dados 
init_db() 
 
# Iniciar o ngrok e a aplicação Flask 
ngrok.set_auth_token("2o2IoIwKJF8eMj0vozQEZLu1kif_5necPSNC7Q7EXqDtibEkq")  # 
Substitua pelo seu authtoken do ngrok 
public_url = ngrok.connect(5000) 
print(f"URL público para a API: {public_url}") 
 
app.run(port=5000)