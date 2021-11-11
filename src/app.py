from flask import Flask, render_template
from livereload import Server

# Instanciando app
app = Flask(__name__)


# Rotas


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/job')
def job():
    return render_template('job.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/curriculum')
def curriculum():
    return render_template('curriculum.html')


# Rodando o app
if __name__ == '__main__':
    server = Server(app.wsgi_app)
    server.serve()
