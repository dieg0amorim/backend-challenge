import jwt
from jwt.exceptions import InvalidTokenError
import math
from flask import Flask, request, jsonify

app = Flask(__name__)

def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def validate_jwt(token):
    try:
        decoded = jwt.decode(token, options={"verify_signature": False})
        
        if len(decoded) != 3:
            return False
        
        if not all(key in decoded for key in ["Name", "Role", "Seed"]):
            return False
        
        if any(char.isdigit() for char in decoded["Name"]) or len(decoded["Name"]) > 256:
            return False
        
        if decoded["Role"] not in ["Admin", "Member", "External"]:
            return False
        
        if not is_prime(int(decoded["Seed"])):
            return False
        
        return True
    except (InvalidTokenError, ValueError):
        return False

@app.route('/validate', methods=['POST'])
def validate():
    data = request.get_json()
    token = data.get('token')
    if not token:
        return jsonify({"valid": False, "error": "Token is missing"}), 400
    
    is_valid = validate_jwt(token)
    return jsonify({"valid": is_valid})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
