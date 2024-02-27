from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')  # ruta principal
def index():
    return render_template('base.html')


@app.route('/home')  # ruta principal
def home():
    return render_template('home.html')


@app.route('/login')  # ruta principal
def login():
    return render_template('login.html')


if __name__ == '__main__':
    app.run(debug=True)
