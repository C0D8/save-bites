from flask_restx import Resource, Namespace
from save_bites.blueprints.restapi.services.alimento import AlimentoService
from flask import request
from flask_restx import fields



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
  
})




@api.route('')
class Alimentos(Resource):

    @api.expect(item)
    def post(self):
        alimento_data = request.json
        return alimento_service.create_alimento(alimento_data)

