from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

gravity_factors = {
    "Mercury": 0.38,
    "Venus": 0.91,
    "Earth": 1.00,
    "Mars": 0.38,
    "Jupiter": 2.34,
    "Saturn": 1.06,
    "Uranus": 0.92,
    "Neptune": 1.19,
    "Pluto": 0.06
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    weight = float(request.form['weight'])
    results = {planet: weight * factor for planet, factor in gravity_factors.items()}
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)