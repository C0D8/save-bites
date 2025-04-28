from save_bites.extensions.serializers import ma
from save_bites.models.alimento import AlimentoModel


class AlimentoSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = AlimentoModel
        load_instance = True
        include_fk = True
        unknown = 'exclude'