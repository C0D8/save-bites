
from marshmallow import ValidationError
from save_bites.schemas.user import UserSchema
from save_bites.schemas.alimento import AlimentoSchema
from flask import abort
from sqlalchemy.exc import IntegrityError




class AlimentoService:

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.alimento_schema = AlimentoSchema()
            cls._instance.user_schema = UserSchema()
        return cls._instance
    



    def create_alimento(self, alimento_data):
        try:
            alimento = self.alimento_schema.load(alimento_data)
            alimento.save_to_db()
        except ValidationError as err:
            # Se ocorrer um erro de validação, retorne uma resposta apropriada
            return {'message': 'Erro ao salvar alimento', 'errors': err.messages}, 400
        except IntegrityError as e:
            # Captura a exceção de integridade referencial
            print(f"IntegrityError: {e}")
            # Verifica se é o problema de chave estrangeira e retorna 404
            if 'foreign key constraint' in str(e):
                abort(404, description="Erro ao salvar alimento. Verifique os dados fornecidos.")
        return {'message': 'Alimento salvo com sucesso'}, 201
    