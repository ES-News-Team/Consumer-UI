from flask import redirect, render_template
from app import consumer_ui_service
import requests


url = 'http://127.0.0.1:5002/news/'


@consumer_ui_service.route('/')
def index():
    return redirect('/pets')


@consumer_ui_service.route('/pets')
def pets_news():
    x = requests.get(url, timeout=3)
    data = x.json()
    pets = {'news': []}
    for element in data['news']:
        if element['type'] == 'Pets':
            pets['news'].append(element)
    return render_template('listagem_noticias.html', **pets)


@consumer_ui_service.route('/artes')
def artes_news():
    x = requests.get(url, timeout=3)
    data = x.json()
    art = {'news': []}
    for element in data['news']:
        if element['type'] == 'Art':
            art['news'].append(element)
    return render_template('listagem_noticias.html', **art)


@consumer_ui_service.route('/ciencias')
def ciencia_news():
    x = requests.get(url, timeout=3)
    data = x.json()
    sci = {'news': []}
    for element in data['news']:
        if element['type'] == 'Sci':
            sci['news'].append(element)
    return render_template('listagem_noticias.html', **sci)
    