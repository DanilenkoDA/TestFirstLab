from flask import Flask, render_template, request, jsonify
import math

app = Flask(__name__)

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise(ValueError)
    return a / b

def modulus(a, b):
    if b == 0:
        raise(ValueError)
    return a % b

def exponentiation(a, b):
    if a == 0 and b == 0:
        raise(ValueError)
    return a ** b

def square_root(a):
    if a < 0:
        raise(ValueError)
    return math.sqrt(a)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/add', methods=['GET'])
def handle_add():
    try:
        a = float(request.args.get('a'))
        b = float(request.args.get('b'))
        result = add(a, b)
        return jsonify({'result': result})
    except (TypeError, ValueError):
        return jsonify({'error': 'Invalid input'}), 400

@app.route('/subtract', methods=['GET'])
def handle_subtract():
    try:
        a = float(request.args.get('a'))
        b = float(request.args.get('b'))
        result = subtract(a, b)
        return jsonify({'result': result})
    except (TypeError, ValueError):
        return jsonify({'error': 'Invalid input'}), 400

@app.route('/multiply', methods=['GET'])
def handle_multiply():
    try:
        a = float(request.args.get('a'))
        b = float(request.args.get('b'))
        result = multiply(a, b)
        return jsonify({'result': result})
    except (TypeError, ValueError):
        return jsonify({'error': 'Invalid input'}), 400

@app.route('/divide', methods=['GET'])
def handle_divide():
    try:
        a = float(request.args.get('a'))
        b = float(request.args.get('b'))
        result = divide(a, b)
        if result == 'Error: Division by zero':
            return jsonify({'error': result}), 400
        return jsonify({'result': result})
    except (TypeError, ValueError):
        return jsonify({'error': 'Invalid input'}), 400

@app.route('/modulus', methods=['GET'])
def handle_modulus():
    try:
        a = float(request.args.get('a'))
        b = float(request.args.get('b'))
        result = modulus(a, b)
        return jsonify({'result': result})
    except (TypeError, ValueError):
        return jsonify({'error': 'Invalid input'}), 400

@app.route('/exponentiation', methods=['GET'])
def handle_exponentiation():
    try:
        a = float(request.args.get('a'))
        b = float(request.args.get('b'))
        result = exponentiation(a, b)
        return jsonify({'result': result})
    except (TypeError, ValueError):
        return jsonify({'error': 'Invalid input'}), 400

@app.route('/sqrt', methods=['GET'])
def handle_sqrt():
    try:
        a = float(request.args.get('a'))
        result = square_root(a)
        if result == 'Error: Square root of negative number':
            return jsonify({'error': result}), 400
        return jsonify({'result': result})
    except (TypeError, ValueError):
        return jsonify({'error': 'Invalid input'}), 400

if __name__ == '__main__':
    app.run(debug=True)
