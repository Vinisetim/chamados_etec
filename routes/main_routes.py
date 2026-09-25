"""
Definição das rotas principais da aplicação (apenas frontend por enquanto).
Utilizamos um Blueprint para modularizar as rotas.
"""
from flask import Blueprint, render_template

# Blueprint principal
main_bp = Blueprint('main', __name__)

@main_bp.route('/')
@main_bp.route('/login')
def login():
    """Rota da tela de login (não herda o base.html completo pois não tem sidebar)."""
    return render_template('login.html')

@main_bp.route('/chamados')
def lista_chamados():
    """Rota da lista geral de chamados."""
    return render_template('lista_chamados.html')

@main_bp.route('/chamados/criar')
def criar_chamado():
    """Rota do formulário para criação de novos chamados."""
    return render_template('criar_chamado.html')

@main_bp.route('/chamados/meus')
def meus_chamados():
    """Rota exclusiva para técnicos visualizarem os chamados atribuídos a eles."""
    return render_template('meus_chamados.html')

@main_bp.route('/usuarios')
def usuarios():
    """Rota de gestão de usuários."""
    return render_template('usuarios.html')
