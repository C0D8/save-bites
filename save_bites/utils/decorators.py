from functools import wraps
from flask import request, g, abort
from save_bites.models.user import User

def with_user_from_clerk_key(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        clerk_key = request.headers.get("Clerk-User-Id")
        if not clerk_key:
            abort(400, description="Clerk-User-Id header ausente")

        user = User.query.filter_by(clerk_key=clerk_key).first()
        if not user:
            abort(404, description="Usuário não encontrado com esse Clerk Key")
        g.current_user = user
        return f(*args, **kwargs)
    return decorated_function
