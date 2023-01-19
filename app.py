import logging
from api.api_views import api_blueprint

import api as api
from flask import Flask, render_template, request, jsonify
from utils import all_information, station

app = Flask(__name__)


@app.route('/')
def main_list():
    schedule = all_information()
    logging.info('Главная страница запрошена')
    return render_template('index.html', schedule=schedule)


@app.route('/page1/<name_st>')
def search(name_st):
    stations = station(name_st)
    # name_st = request.args.get('s')
    # stations = station(name_st)
    logging.info('Осуществляется поиск по слову')
    return render_template('search.html', stations=stations)


logging.basicConfig(filename="log.logs", level=logging.INFO, encoding="utf-8", format="%(asctime)s : %(levelname)s : %(message)s")
app.register_blueprint(api_blueprint)

@app.errorhandler(404)
def error_404(e):
    return 'Страница не сущестует', 404


@app.errorhandler(500)
def error_500(e):
    return 'Ошибка на стороне сервера', 500




if __name__ == '__main__':
    app.run()