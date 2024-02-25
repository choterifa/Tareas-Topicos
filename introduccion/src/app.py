from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def bienvenido():
    mensaje = 'Bienvenido al sitio Web Carlos Eduardo Valencia'
    return render_template('bienvenida.html', mensaje=mensaje)


if __name__ == '__main__':
    app.run(debug=True)
