# Use a imagem oficial do Python como base
FROM python:3.10-slim

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Copie o arquivo de requisitos para o diretório de trabalho
COPY requirements.txt .

# Instale as dependências do Python
RUN pip install --no-cache-dir -r requirements.txt

# Copie o código da aplicação para o diretório de trabalho
COPY . .

# Exponha a porta que o FastAPI usará
EXPOSE 8000

# Comando para rodar a aplicação
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
