from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/porta')
def porta():
    return render_template('porta.html')


@app.route('/acerca')
def acerca():
    return render_template('acerca.html')


@app.route('/contacto')
def contacto():
    return render_template('contacto.html')

if __name__ == '__main__':
    app.run(port=5020)