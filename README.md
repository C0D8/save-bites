# save-bites



Para rodar via docker:


docker copose up -d -- build na pasta rais do projeto



Para rodar localmente em seu computador, instale as dependências com o comando:

```bash
pip install -r requirements.txt
```

crie o .env com as variáveis de ambiente necessárias indicadas no arquivo .env.example

lembre-se de criar o banco de dados em sua máquina 


por fim, realize as migrações com o comando:

```bash
flask db init
flask db migrate
flask db upgrade
```

rode o projeto com o comando:

```bash
flask run --reload
```

acesse em http://localhost:5006/ para ver a documentação da API