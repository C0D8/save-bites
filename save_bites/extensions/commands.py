import click
from save_bites.extensions.db import db
from dotenv import load_dotenv
import os
from save_bites.models.user import User, Role
#import hashpassword 
from werkzeug.security import generate_password_hash
from flask import current_app
load_dotenv()


def create_admin():
#     """Creates database tables"""
    with current_app.app_context():
#         # db.create_all()
#         # adicionar a criação das roles iniciais
        admin_role = Role(name="admin")
        admin_user = User(password=generate_password_hash(os.getenv("ADMIN_PASSWORD")), roles=[admin_role], username= os.getenv("ADMIN_USERNAME"), clerk_key=os.getenv("ADMIN_USERNAME"))
        db.session.add(admin_role)
        db.session.add(admin_user)
        db.session.commit()
    print("Admin created")

def drop_db():
    """Cleans database"""
    db.drop_all()
    print("Tables dropped")


def create_super_user():
    """Creates a super user"""
    admin_username = os.getenv("ADMIN_USERNAME")
    admin_password = os.getenv("ADMIN_PASSWORD")

    with current_app.app_context():
        # Verifica se a role "admin" já existe, se não, cria
        admin_role = Role.query.filter_by(name="admin").first()
        if not admin_role:
            admin_role = Role(name="admin")
            db.session.add(admin_role)
            db.session.commit()
            print("✅ Role 'admin' criada.")

        # Verifica se o usuário já existe
        admin_user = User.query.filter_by(username=admin_username).first()

        if not admin_user:
            admin_user = User(
                username=admin_username,
                password=generate_password_hash(admin_password)
            )
            admin_user.roles.append(admin_role)  # Associa o usuário à role "admin"

            db.session.add(admin_user)
            db.session.commit()
            print("✅ Super user criado.")
        else:
            print("ℹ️ Super user já existe.")



def init_app(app):
    for command in [create_admin, drop_db, create_super_user]:
        app.cli.add_command(app.cli.command()(command))

    @app.cli.command()
    @click.option("-username", "-u", prompt=True)
    @click.option(
        "-password", "-p", prompt=True, hide_input=True, confirmation_prompt=True
    )
    def create_simple_user(username, password):
        """Creates a simple user"""
        user = User.query.filter_by(username=username).first()
        if not user:
            user = User(username=username, password=generate_password_hash(password))
            user.roles.append(Role.query.filter_by(name="admin").first())
            db.session.add(user)
            db.session.commit()
            print("Simple user created")
        else:
            print("Simple user already exists")
