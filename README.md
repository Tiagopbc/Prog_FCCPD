# Prog_FCCPD

## Rodando com Docker Compose (recomendado)

1. Clone o repositório e acesse a pasta do projeto:
   ```powershell
   cd "caminho/para/Prog_FCCPD"
   ```

2. Suba os containers (isso irá criar e popular o banco automaticamente):
   ```powershell
   docker-compose up --build
   ```

4. Para reiniciar e resetar o banco (apaga tudo):
   ```powershell
   docker-compose down -v
   docker-compose up --build
   ```

## Rodando em outro terminal

1. Instale as dependências:
   ```powershell
   pip install -r requirements.txt
   ```

5. Rode o sistema:
   ```powershell
   python app.py
   ```