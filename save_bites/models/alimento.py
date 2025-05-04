from save_bites.extensions.db import db


class AlimentoModel(db.Model):
    __tablename__ = 'alimento'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(255), nullable=True)
    descricao = db.Column(db.String(255), nullable=True)
    data_validade = db.Column(db.DateTime, nullable=True)
    quantidade = db.Column(db.Integer, nullable=True)
    valor = db.Column(db.Float, nullable=True)
    categoria = db.Column(db.String(255), nullable=True)    
    tag = db.Column(db.String(255), nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)
    user = db.relationship('User', back_populates='alimentos') 

    @classmethod
    def find_all(cls):
        return cls.query.all()
    
    @classmethod
    def find_by_user_id(cls, user_id):
        return cls.query.filter_by(user_id=user_id).all()
    
    @classmethod
    def find_by_id_and_user_id(cls, id, user_id):
        return cls.query.filter_by(id=id, user_id=user_id).first()
    

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
    
    def update_to_db(self):
        db.session.commit()
