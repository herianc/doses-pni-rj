from flask import Flask, render_template
import pymysql

app = Flask(__name__)

# Configuração do banco
db = pymysql.connect(
    host="localhost",
    user="usuario",
    password="senha123",
    database="meubanco",
    port=3306
)

@app.route("/")
def home():
    cursor = db.cursor()
    cursor.execute("SHOW TABLES;")
    tabelas = [t[0] for t in cursor.fetchall()]  # lista de tabelas
    return render_template("index.html", tabelas=tabelas)

@app.route("/tabela/<nome>")
def mostrar_tabela(nome):
    cursor = db.cursor()
    cursor.execute(f"SELECT * FROM {nome};")
    dados = cursor.fetchall()
    colunas = [desc[0] for desc in cursor.description]
    return render_template("tabela.html", dados=dados, colunas=colunas, nome=nome)

app.run(debug=True)
