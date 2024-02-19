from flask import Flask, render_template
import json

app = Flask(__name__)


@app.route('/list_prof/<list>')
def output(list):
    with open("templates/jobs.json", "rt", encoding="utf-8") as f:
        jobs = json.loads(f.read())
    return render_template("list.html", jobs=jobs, list=list)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1', debug=True)
