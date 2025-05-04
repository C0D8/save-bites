from flask_restx import Resource, Namespace
from save_bites.blueprints.restapi.services.alimento import AlimentoService
from flask import request, g
from flask_restx import fields
from save_bites.utils.decorators import with_user_from_clerk_key




api = Namespace('alimentos', description='Alimentos operations')



alimento_service = AlimentoService()

item = api.model('Alimento', {
    "nome" : fields.String("Nome do alimento", required=True),
    "descricao" : fields.String("Descrição do alimento", required=False),
    "data_validade" : fields.DateTime("Data de validade do alimento", required=True),
    "quantidade" : fields.Integer(2, required=True),
    "valor" : fields.Float("10.5", required=False),
    "categoria" : fields.String("Categoria do alimento", required=False),
    "tag" : fields.String("Tag do alimento", required=False)
  
}, header={
    "user_id": fields.String("ID do usuário", required=True)
})




@api.route('')
class Alimentos(Resource):

    @api.expect(item)
    @with_user_from_clerk_key
    def post(self):
        alimento_data = request.json
        user_id = g.current_user.id
        alimento_data['user_id'] = user_id
        return alimento_service.create_alimento(alimento_data)
    
    @with_user_from_clerk_key
    def get(self):
        user_id = g.current_user.id
        return alimento_service.get_alimentos(user_id)
    

@api.route('/<int:alimento_id>')
class Alimento(Resource):

    @with_user_from_clerk_key
    def delete(self, alimento_id):
        user_id = g.current_user.id
        return alimento_service.delete_alimento(alimento_id, user_id)
    