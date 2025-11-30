# 🐬 Trabalho Final de Banco de Dados 

## Sobre o trabalho
Este repositório contém o trabalho final da disciplina de **Banco de Dados (ICP489)** do semestre 2025.2 
do curso de Ciência da Computação da Universidade Federal do Rio de Janeiro.    
   
Este trabalho utiliza dados do Open Data SUS, especificamente, dados do [Programa Nacional de Imunizações (PNI) de 2024](https://opendatasus.saude.gov.br/dataset/doses-aplicadas-pelo-programa-de-nacional-de-imunizacoes-pni-2024).
Tendo em vista o seu grande volume, este projeto restringe-se apenas a uma amostra (cerca de 130 mil) de aplicações feitas no Estado do Rio de Janeiro.

## 📁 Estrutura do projeto

```bash
├── 📁 app
│   ├── 🐍 app.py
│   ├── 📁 assets
│   │   ├──  logo_dcc.png
│   │   ├──  unidade.png
│   │   └──  vacina.jpg
│   ├── 📁 utils
│   │   ├──  constants.py
│   │   └──  db_functions.py
│   └── 📁 views
│       ├──  1_home.py
│       ├──  2_painel.py
│       ├──  3_estatisticas.py
│       └──  4_debug.py
├── 📁 db
│   ├── init.sql
│   └── 📁 modelagem
│       ├──  BD_MODELAGEM_CONCEITUAL.png
│       ├──  BD_MODELAGEM_LOGICA.png
│       ├──  Conceitual_1.brM3
|       └─── Lógico_1.brM3
```

A pasta `/db` contém o arquivo `init.sql` utilizado quando o docker compose é inicializado pela primeira vez, este script sql cria as tabelas e popula o banco com os registros utilizados no trabalho.
Além disso, este diretório também armazena os arquivos de modelagem lógica e conceitual do banco de dados. 

Já a pasta `/app` contém toda a estrutura da aplicação web, sendo o arquivo `app.py` o responsável por iniciar a aplicação. 

## ⬇️ Instalação

Após clonar o repositório replique os comandos abaixo.

### Subindo imagem docker com o MySQL

Para subir o container com a imagem do banco MySQL 

```bash
docker compose up -d 
```

### Instalando depedências com UV
```bash
uv sync
```

### Rodando a aplicação localmente

```bash
cd app
uv run streamlit run app.py
```

## Imagens da aplicação
### Painel 
![](https://github.com/herianc/icp489-banco-de-dados/blob/main/images/screenshot_dash.png?raw=true)


### Estatísticas de 2024
![a](https://github.com/herianc/icp489-banco-de-dados/blob/main/images/screenshot_stats.png?raw=true)

