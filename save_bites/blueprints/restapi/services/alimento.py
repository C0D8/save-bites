
from marshmallow import ValidationError
from save_bites.models.alimento import AlimentoModel
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
            cls._instance.alimentos_model = AlimentoModel()
        return cls._instance

    def create_alimento(self, alimento_data):
        try:
            alimento = self.alimento_schema.load(alimento_data)
            alimento.save_to_db()
        except ValidationError as err:
            return {'message': 'Erro ao salvar alimento', 'errors': err.messages}, 400
        except IntegrityError as e:
            print(f"IntegrityError: {e}")
            if 'foreign key constraint' in str(e):
                abort(404, description="Erro ao salvar alimento. Verifique os dados fornecidos.")
        return {'message': 'Alimento salvo com sucesso'}, 201

    def get_alimentos(self, user_id=None):
        if user_id:
            try:
                alimentos = self.alimentos_model.find_by_user_id(user_id)
                result = self.alimento_schema.dump(alimentos, many=True)
                return result
            except ValidationError as err:
                return {'message': 'Erro ao buscar alimentos', 'errors': err.messages}, 400
            except IntegrityError as e: 
                print(f"IntegrityError: {e}")
                if 'foreign key constraint' in str(e):
                    abort(404, description="Erro ao buscar alimentos. Verifique os dados fornecidos.")
            return {'message': 'Alimentos encontrados com sucesso'}, 200
        else:
            return {'message': 'Erro ao buscar alimentos. Verifique os dados fornecidos.'}, 400
        
    def delete_alimento(self, alimento_id, user_id):
        try:
            alimento = self.alimentos_model.find_by_id_and_user_id(alimento_id, user_id)
            if not alimento:
                abort(404, description="Alimento não encontrado")
            alimento.delete_from_db()
        except ValidationError as err:
            return {'message': 'Erro ao deletar alimento', 'errors': err.messages}, 400
        except IntegrityError as e:
            print(f"IntegrityError: {e}")
            if 'foreign key constraint' in str(e):
                abort(404, description="Erro ao deletar alimento. Verifique os dados fornecidos.")
        return {'message': 'Alimento deletado com sucesso'}, 200
    
    def update_alimento(self, alimento_id, user_id, alimento_data):
        try:
            alimento = self.alimentos_model.find_by_id_and_user_id(alimento_id, user_id)
            if not alimento:
                abort(404, description="Alimento não encontrado")
            for key, value in alimento_data.items():
                setattr(alimento, key, value)
            alimento.update_to_db()
        except ValidationError as err:
            return {'message': 'Erro ao atualizar alimento', 'errors': err.messages}, 400
        except IntegrityError as e:
            print(f"IntegrityError: {e}")
            if 'foreign key constraint' in str(e):
                abort(404, description="Erro ao atualizar alimento. Verifique os dados fornecidos.")
        return {'message': 'Alimento atualizado com sucesso'}, 200
    
    def get_alimento_by_id(self, alimento_id, user_id):
        try:
            alimento = self.alimentos_model.find_by_id_and_user_id(alimento_id, user_id)
            if not alimento:
                abort(404, description="Alimento não encontrado")
            result = self.alimento_schema.dump(alimento)
        except ValidationError as err:
            return {'message': 'Erro ao buscar alimento', 'errors': err.messages}, 400
        except IntegrityError as e:
            print(f"IntegrityError: {e}")
            if 'foreign key constraint' in str(e):
                abort(404, description="Erro ao buscar alimento. Verifique os dados fornecidos.")
        return result
    

