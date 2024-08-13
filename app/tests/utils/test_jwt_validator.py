from utils.jwt_validator import JWTValidator

def test_validate_jwt():
    validator = JWTValidator()
    valid_token = jwt.encode({"Name": "Alice", "Role": "Member", "Seed": "17"}, key='secret')
    invalid_token = "invalid_token"
    
    assert validator.validate(valid_token) == True
    assert validator.validate(invalid_token) == False
