from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "HELLO!!! WORLD!!"

@app.route('/dojo')
def dojo():
    return "DojO!!"

@app.route('/say/<name>')
def say_hello(name):
    return "Hi! " + name

@app.route('/repeat/<num>/<word>')
def repeat(num, word):
    return "nums x word: " + int(num) * word




if __name__ == ('__main__'):
    app.run(debug=True)