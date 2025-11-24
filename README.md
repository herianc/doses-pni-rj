# Trabalho Final de Banco de Dados 


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