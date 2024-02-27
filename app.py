from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')  # ruta principal
def index():
    return render_template('base.html')


@app.route('/hero')  # ruta principal
def hero():
    return render_template('hero.html')


@app.route('/sobremi')  # ruta principal
def sobremi():
    return render_template('sobremi.html')


@app.route('/experiencia')  # ruta principal
def experiencia():
    return render_template('experiencia.html')


@app.route('/proyectos')  # ruta principal
def proyectos():
    return render_template('proyectos.html')


@app.route('/login')  # ruta principal
def login():
    return render_template('login.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)
