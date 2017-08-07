import loggin

from flask import Flask
from flask import request

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello World!'

@app.route('/predict')
def predict():
    captchaString = request.args.get('captchaString')
    return captchaString;

@app.errorhandler(500)
def server_error(e):
    logging.exception('An error occurred during a request.')
    return """
    An internal error occurred: <pre>{}</pre>
    See logs for full stacktrace.
    """.format(e), 500


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)