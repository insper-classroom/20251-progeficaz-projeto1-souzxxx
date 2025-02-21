from flask import Flask, render_template_string, request, redirect, render_template
import sqlite3 as sql


app = Flask(__name__)

# Configurando a pasta de arquivos estáticos
app.static_folder = 'static'

@app.route('/')
def index():
    con = sql.connect('banco.db')
    con.row_factory = sql.Row
    cur = con.cursor()
    cur.execute('SELECT * FROM texto')
    data=cur.fetchall()
    return render_template('index.html', data=data)

@app.route('/submit', methods=['POST'])
def submit_form():
    titulo = request.form['titulo']
    detalhes = request.form['detalhes']
    con = sql.connect('banco.db')
    cur = con.cursor()
    cur.execute('INSERT INTO texto (titulo, detalhes) VALUES (?, ?)', (titulo, detalhes))
    con.commit()
    return redirect('/')

@app.route('/delete/<int:id>', methods=['POST'])
def delete(id):
    con = sql.connect('banco.db')
    cur = con.cursor()
    cur.execute('DELETE FROM texto WHERE id = ?', (id,))
    con.commit()
    return redirect('/')

@app.route('/edit/<int:id>', methods=['POST'])
def edit(id):
    con = sql.connect('banco.db')
    con.row_factory = sql.Row
    cur = con.cursor()
    cur.execute('SELECT * FROM texto WHERE id = ?', (id,))
    data=cur.fetchone()
    return render_template('edit.html', data=data)

@app.route('/update/<int:id>', methods=['POST'])
def update(id):
    titulo = request.form['titulo']
    detalhes = request.form['detalhes']
    con = sql.connect('banco.db')
    cur = con.cursor()
    cur.execute('UPDATE texto SET titulo = ?, detalhes = ? WHERE id = ?', (titulo, detalhes, id))
    con.commit()
    return redirect('/')
if __name__ == '__main__':
    app.run(debug=True)