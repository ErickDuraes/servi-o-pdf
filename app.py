from flask import Flask
from src.routes.pdf_routes import pdf_bp

def create_app():
    app = Flask(__name__)
    
    # Registra as rotas de PDF com prefixo /pdf
    app.register_blueprint(pdf_bp, url_prefix='/pdf')
    
    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)