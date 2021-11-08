from flask import Flask, render_template

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
    app.run(debug=True)
