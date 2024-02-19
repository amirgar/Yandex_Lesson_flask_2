from flask import Flask, render_template
import json

app = Flask(__name__)


@app.route('/list_prof/answer')
@app.route('/list_prof/auto_answer')
def output():
    with open("templates/package.json", "rt", encoding="utf-8") as f:
        params = json.loads(f.read())  # автоматическое заполнение
    with open("templates/user.json", "rt", encoding="utf-8") as f:
        user = json.loads(f.read())  # пользовательские настройки
    return render_template("auto_answer.html", m=user, p=params)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1', debug=True)
