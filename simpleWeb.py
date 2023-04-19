from flask import Flask, request, render_template, jsonify, _app_ctx_stack

app = Flask(__name__, static_folder='static', template_folder='template')

@app.route('/')
def hello():
    return 'Hello'

@app.route('/hi')
def hi():
    return 'Hi~~~'

@app.route('/sample')
def sample():
    return render_template('sample.html')

if __name__ == '__main__':
    app.run(
    host="127.0.0.1",
    port=7777,
    debug=True)