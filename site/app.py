from flask import Flask, render_template
import pymysql

app = Flask(__name__)


def get_db_connection():
    """Função auxiliar para criar uma conexão."""
    return pymysql.connect(
        host="127.0.0.1",
        user="usuario",
        password="senha123",
        database="meubanco",
        port=3310
    )

@app.route("/")
def home():
    db = get_db_connection()
    try:
        with db.cursor() as cursor:
            cursor.execute("SHOW TABLES;")
            tabelas = [t[0] for t in cursor.fetchall()]
    finally:
        db.close() 

    return render_template("index.html", tabelas=tabelas)

@app.route("/tabela/<nome>")
def mostrar_tabela(nome):
    db = get_db_connection() 
    try:
        with db.cursor() as cursor:
            
            cursor.execute("SHOW TABLES;")
            tabelas_validas = [t[0] for t in cursor.fetchall()]

            if nome not in tabelas_validas:
                return "Erro: Tabela inválida!", 404 
            
            cursor.execute(f"SELECT * FROM {nome};")
            dados = cursor.fetchall()
            colunas = [desc[0] for desc in cursor.description]


    finally:
        db.close() 

    return render_template("tabela.html", dados=dados, colunas=colunas, nome=nome)

if __name__ == "__main__": 
    app.run(debug=True)