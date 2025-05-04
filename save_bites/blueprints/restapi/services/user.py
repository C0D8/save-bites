
from marshmallow import ValidationError
from save_bites.schemas.user import UserSchema
from flask import abort
from sqlalchemy.exc import IntegrityError
from save_bites.models.user import User




class UserService:

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.user_schema = UserSchema()
            cls._instance.user_model= User()
        return cls._instance

    def create_user_by_clerk_hook(self, user_data):
        """
        Cria um usuário no banco de dados a partir do webhook do Clerk.
        """
        try:
            user = self.user_schema.load(user_data)
            user.save_to_db()
        except ValidationError as err:
            return {'message': 'Erro ao salvar usuário', 'errors': err.messages}, 400
        except IntegrityError as e:
            print(f"IntegrityError: {e}")
            if 'foreign key constraint' in str(e):
                abort(404, description="Erro ao salvar usuário. Verifique os dados fornecidos.")
        return {'message': 'Usuário salvo com sucesso'}, 201

        
