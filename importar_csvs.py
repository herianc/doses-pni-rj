import pandas as pd
import pymysql
import os

conn = pymysql.connect(
    host="127.0.0.1",
    user="usuario",
    password="senha123",
    database="meubanco",
    port=3310
)

pasta = "populacao"
print(f"A ler ficheiros da pasta: {pasta}")

try:
    with conn.cursor() as cursor:
        
        print("Desabilitando verificação de chaves estrangeiras...")
        cursor.execute("SET FOREIGN_KEY_CHECKS = 0")

        print("Verificando tabelas existentes no banco...")
        cursor.execute("SHOW TABLES;")
        tabelas_reais = {row[0] for row in cursor.fetchall()}
        print(f"Tabelas encontradas: {tabelas_reais}")
        
        for arquivo in os.listdir(pasta):
            if arquivo.endswith(".csv"):
                caminho = os.path.join(pasta, arquivo)
                tabela = arquivo.replace(".csv", "")

                if tabela == "AplicacaoDose":
                    tabela_correta = "_AplicacaoDose_Estabelecimento_Vacina_Paciente"
                    if tabela_correta in tabelas_reais:
                        print(f"HOTFIX: Mapeando '{arquivo}' para a tabela '`{tabela_correta}`'...")
                        tabela = tabela_correta 
                    else:
                        print(f"AVISO: O arquivo '{arquivo}' seria mapeado para '`{tabela_correta}`', mas esta tabela não existe.")
                        continue 

                if tabela not in tabelas_reais:
                    print(f"AVISO: O arquivo '{arquivo}' será ignorado, pois a tabela '`{tabela}`' não existe no banco.")
                    continue 

                print(f"A processar {arquivo} para a tabela {tabela}...")

                if tabela == "Paciente":
                    try:
                        print("HOTFIX: Alterando 'Paciente.uf' para VARCHAR(255)...")
                        cursor.execute("ALTER TABLE Paciente MODIFY COLUMN uf VARCHAR(255)")
                    except Exception as e:
                        print(f"Não foi possível alterar a tabela (talvez já esteja correta): {e}")

                df = pd.read_csv(caminho, sep=';') 

                colunas_para_remover = []
                renames = {}

                whitelist_id_fabricante = {'Fabricante', 'fabrica'}

                if tabela == "_AplicacaoDose_Estabelecimento_Vacina_Paciente":
                    if 'data_aplicacao' in df.columns:
                        renames['data_aplicacao'] = 'data_vacina'
                    if 'cod_lote_vacina' in df.columns:
                        renames['cod_lote_vacina'] = 'lote_vacina'

                elif tabela == "fabrica":
                    if 'cod_fabricante' in df.columns:
                        renames['cod_fabricante'] = 'id_fabricante'
                
                if tabela != "fabrica" and 'cod_fabricante' in df.columns:
                    colunas_para_remover.append('cod_fabricante')
                
                if tabela not in whitelist_id_fabricante and 'id_fabricante' in df.columns:
                    colunas_para_remover.append('id_fabricante')
                
                if colunas_para_remover:
                    print(f"HOTFIX: Removendo colunas (não existem no banco): {colunas_para_remover}...")
                    df = df.drop(columns=colunas_para_remover)
                
                if renames:
                    print(f"HOTFIX: Renomeando colunas: {renames}")
                    df = df.rename(columns=renames)

                df = df.astype(object).where(pd.notnull(df), None)

                print(f"Limpando a tabela `{tabela}`...")
                cursor.execute(f"TRUNCATE TABLE `{tabela}`") 

                colunas = ', '.join([f"`{c}`" for c in df.columns])
                placeholders = ', '.join(['%s'] * len(df.columns))
                
                sql = f"INSERT IGNORE INTO `{tabela}` ({colunas}) VALUES ({placeholders})"
                
                print(f"A inserir {len(df)} linhas em `{tabela}`...")
                
                for _, row in df.iterrows():
                    cursor.execute(sql, tuple(row))
        
        print("Reabilitando verificação de chaves estrangeiras...")
        cursor.execute("SET FOREIGN_KEY_CHECKS = 1")
        
        conn.commit()
        print("\nImportação concluída com sucesso!")

finally:
    conn.close()
    print("Conexão fechada.")