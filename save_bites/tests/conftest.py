import pytest
from dynaconf import settings
from save_bites.app import create_app, minimal_app
from save_bites.extensions.db import db


@pytest.fixture(scope="function")  
def setup_env(monkeypatch):
   
    #Configurar variaveis de ambiente para que o dynaconf não pertube
    monkeypatch.setenv('POSTGRES_USER', 'testuser')
    monkeypatch.setenv('POSTGRES_PASSWORD', 'testpassword')
    monkeypatch.setenv('POSTGRES_HOST', 'localhost')
    monkeypatch.setenv('POSTGRES_PORT', '5432')
    monkeypatch.setenv('POSTGRES_DATABASE', 'testdb')
    

@pytest.fixture(scope="function")  
def min_app(setup_env):
    settings.configure(FORCE_ENV_FOR_DYNACONF="testing")
    app = minimal_app(FORCE_ENV_FOR_DYNACONF="testing")
    return app

@pytest.fixture(scope="function")  
def app(setup_env):
    settings.configure(FORCE_ENV_FOR_DYNACONF="testing")
    settings.configure(TESTING=True)
    settings.configure(ENV='testing')
    app = create_app(FORCE_ENV_FOR_DYNACONF="testing")
    print(f"Ambiente Dynaconf carregado: {app.config['ENV_FOR_DYNACONF']}")
    with app.app_context():
        db.create_all()
        yield app
        db.drop_all()
