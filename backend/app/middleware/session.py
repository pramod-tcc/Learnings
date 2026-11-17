from starlette.middleware.sessions import SessionMiddleware
from app.core.config import SESSION_SECRET_KEY 

def setup_session(app):
    app.add_middleware(SessionMiddleware, 
                       secret_key=SESSION_SECRET_KEY,
                       same_site="lax",
                       https_only=False)
