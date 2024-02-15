from flask import Flask, render_template

app = Flask(__name__)


@app.route('/<title>')
@app.route('/index/<title>')
def index(title):
    sample_text = ""
    return render_template("base.html", title=title, sample_text=sample_text)


@app.route('/training/<prof>')
def location(prof):
    return render_template("prof.html", prof=prof)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1', debug=True)
