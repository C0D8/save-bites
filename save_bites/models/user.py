from save_bites.extensions.db import db

user_roles = db.Table('user_roles',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True),
    db.Column('role_id', db.Integer, db.ForeignKey('role.id'), primary_key=True)
)

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True, nullable=True)
    username = db.Column(db.String(255), unique=True, nullable=True)
    password = db.Column(db.String(255), nullable=True)
    roles = db.relationship('Role', secondary='user_roles',
                         backref='users', lazy='dynamic')
    alimentos = db.relationship('AlimentoModel', back_populates='user')
    clerk_key = db.Column(db.String(255), unique=True, nullable=False, index=True)

    def json(self):return {"username": self.username, "roles": self.roles, "id": self.id} 

    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()
    
    
    def check_password(self, password):
        return self.password == password

    @classmethod
    def find_all(cls):
        return cls.query.all()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
    
    def update_to_db(self):
        db.session.commit()


class Role(db.Model):
    __tablename__ = 'role'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))
