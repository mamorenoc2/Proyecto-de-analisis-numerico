from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/funciones')
def inicio_funciones():
    return render_template('inicio.html')


@app.route('/sobre_proyecto')
def sobre_proyecto():
    return render_template('sobre_proyecto.html')


app.run(host='0.0.0.0', port=81, debug=True)
