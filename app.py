
from flask import Flask, jsonify
import socket

from square import Square

app = Flask(__name__)

@app.route('/')
def health():
    return jsonify({"status":"true"})

@app.route('/greeting')
def greeting():
    hostname = socket.gethostname()
    return 'Hello World from ' + hostname

@app.route('/square/<int:x>')
def square(x=0):
    result = Square(x, x**2).toJson()
    return result

if __name__ == '__main__':
    app.run(debug=True, port=80,host='0.0.0.0')