import os
from flask import Flask, redirect, request, abort
from werkzeug.exceptions import BadRequest

from classes.search import Search
from config import DATA_DIR

app = Flask(__name__)


@app.route("/")
def index():
    return redirect('/perform_query/?cmd1=filter&value1=GET&cmd2=limit&value2=5')


@app.route("/perform_query/", methods=['GET', 'POST'])
def perform_query():
    # Получить команды из запроса
    try:
        cmd1 = request.args.get('cmd1')
        value1 = request.args.get('value1')
        cmd2 = request.args.get('cmd2')
        value2 = request.args.get('value2')
    except KeyError:
        raise BadRequest()
    if not os.path.exists(DATA_DIR):
        return BadRequest(description=f"Передано не неверное имя файла")

    # Выполнять команды
    try:
        with open(DATA_DIR, 'r') as file:
            first_result = getattr(Search, cmd1)(file, value1)
            second_result = getattr(Search, cmd2)(first_result, value2)
    except (ValueError, TypeError) as e:
        abort(400, e)

    return app.response_class(second_result, content_type="text/plain")


if __name__ == '__main__':
    app.run(debug=True)
