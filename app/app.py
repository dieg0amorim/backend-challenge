from flask import Flask, request, jsonify
from prometheus_flask_exporter import PrometheusMetrics
from utils.jwt_validator import JWTValidator

app = Flask(__name__)
metrics = PrometheusMetrics(app)

jwt_validator = JWTValidator()

@app.route('/validate', methods=['POST'])
def validate():
    data = request.get_json()
    token = data.get('token')
    if not token:
        return jsonify({"valid": False, "error": "Token is missing"}), 400
    
    is_valid = jwt_validator.validate(token)
    return jsonify({"valid": is_valid})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
