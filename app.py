"""
Script inicializador da aplicação Flask.
Configura as pastas de templates e arquivos estáticos e registra as rotas (blueprints).
"""
import os
from flask import Flask

def create_app():
    # Inicializa o app apontando para a pasta frontend para templates e static
    base_dir = os.path.abspath(os.path.dirname(__file__))
    app = Flask(
        __name__,
        template_folder=os.path.join(base_dir, 'frontend', 'templates'),
        static_folder=os.path.join(base_dir, 'frontend', 'static')
    )

    # Registro das rotas via Blueprints
    from routes.main_routes import main_bp
    app.register_blueprint(main_bp)

    return app

if __name__ == '__main__':
    app = create_app()
    # Roda em modo debug para desenvolvimento
    app.run(debug=True)
