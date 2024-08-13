# Use a imagem base do Python
FROM python:3.11-slim

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Copia o arquivo requirements.txt para o container
COPY requirements.txt .

# Instala as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copia o restante dos arquivos da aplicação para o container
COPY . .

# Expõe a porta 5000
EXPOSE 5000

# Define o comando de inicialização do container
CMD ["python", "app.py"]