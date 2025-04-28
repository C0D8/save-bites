def test_environment_variables(app):
    """
    Testa se as variáveis de ambiente estão corretamente configuradas.
    """
    assert app.config['FORCE_ENV_FOR_DYNACONF'] == "testing", "A variável FORCE_ENV_FOR_DYNACONF deve ser 'testing'."
    assert app.config['SQLALCHEMY_DATABASE_URI'] == "sqlite:///testing.db", "A variável SQLALCHEMY_DATABASE_URI deve ser 'sqlite:///test.db'."


def test_banco_vazio(app):

    with app.test_client() as client:
        response = client.get('/api/contratos')
        json_response = response.get_json()
        assert json_response == [], "O banco de dados deve estar vazio."