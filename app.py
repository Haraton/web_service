from flask import Flask, request, redirect, url_for, jsonify, session, make_response
import json

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    return "主页"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
