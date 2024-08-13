import jwt
from jwt.exceptions import InvalidTokenError
from utils.prime_checker import PrimeChecker

class JWTValidator:
    def __init__(self):
        self.prime_checker = PrimeChecker()

    def validate(self, token):
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
            
            if not self.prime_checker.is_prime(int(decoded["Seed"])):
                return False
            
            return True
        except (InvalidTokenError, ValueError):
            return False
