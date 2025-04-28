from save_bites.extensions.serializers import ma
from save_bites.models.user import User




class UserSchema(ma.SQLAlchemyAutoSchema):
    
    class Meta:
        model = User
        load_instance = True
        include_fk = True
        unknown = 'exclude'

