# Usa uma imagem base do Python
FROM python:3.8-slim

# Configuração do ambiente de trabalho
WORKDIR /app

# Copia os arquivos de requerimentos para o container
COPY requirements.txt .

# Instala as dependências do aplicativo
RUN pip install --no-cache-dir -r requirements.txt

# Copia todos os arquivos do diretório local para o container
COPY . .

# Expõe a porta em que o aplicativo estará rodando
EXPOSE 5000

# Comando para rodar o aplicativo
CMD ["python", "app.py"]
