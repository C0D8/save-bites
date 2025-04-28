FROM python:3.11

WORKDIR /app

# Atualiza os pacotes e instala dependências necessárias
RUN apt-get update && apt-get install -y libgl1-mesa-glx

# Copia o arquivo de requisitos para o contêiner
COPY requirements.txt .

# Instala as dependências do Python
RUN pip3 install --no-cache-dir -r requirements.txt --timeout=100

# Copia o restante da aplicação para o contêiner
COPY . .

# Copia o script wait-for-it.sh para o contêiner
# COPY wait-for-it.sh /wait-for-it.sh
# RUN chmod +x /wait-for-it.sh

# Define a variável de ambiente FLASK_APP
ENV FLASK_APP=save_bites/app.py 

# Define o comando para aguardar o MySQL e iniciar o Flask com as migrações

CMD flask db upgrade && flask create-super-user && flask run --host=0.0.0.0 --port=5005