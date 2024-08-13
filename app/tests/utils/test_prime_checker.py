from utils.prime_checker import PrimeChecker

def test_is_prime():
    checker = PrimeChecker()
    assert checker.is_prime(2) == True
    assert checker.is_prime(15) == False
    assert checker.is_prime(17) == True