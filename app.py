from flask import Flask, render_template, request, redirect, url_for
import sqlite3
import os

app = Flask(__name__)
DB_PATH = "database.db"

# Inicializa o banco de dados
def init_db():
    if not os.path.exists(DB_PATH):
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE economia (
                          id INTEGER PRIMARY KEY AUTOINCREMENT,
                          valor REAL,
                          data TEXT DEFAULT CURRENT_TIMESTAMP)''')
        conn.commit()
        conn.close()

@app.route('/')
def index():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM economia ORDER BY data DESC")
    historico = cursor.fetchall()
    cursor.execute("SELECT SUM(valor) FROM economia")
    total = cursor.fetchone()[0] or 0
    meta = 20000  # Meta de economia
    conn.close()
    return render_template('index.html', historico=historico, total=total, meta=meta)

@app.route('/add', methods=['POST'])
def add():
    valor = request.form.get('valor')
    if valor:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO economia (valor) VALUES (?)", (valor,))
        conn.commit()
        conn.close()
    return redirect(url_for('index'))

@app.route('/delete/<int:id>')
def delete(id):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM economia WHERE id = ?", (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

@app.route('/dicas')
def dicas():
    videos = [
        {"titulo": "Como economizar dinheiro rápido", "url": "https://www.youtube.com/embed/example1"},
        {"titulo": "Dicas para juntar dinheiro", "url": "https://www.youtube.com/embed/example2"}
    ]
    return render_template('dicas.html', videos=videos)

@app.route('/sobre')
def sobre():
    return render_template('sobre.html')

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
