from flask import render_template
from app import consumer_ui_service

@consumer_ui_service.route('/')
def index():
    return render_template('listagem_noticias.html', test='OwO')
