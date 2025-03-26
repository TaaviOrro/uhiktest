import unittest

# Parandatud matemaatiliste arvutuste funktsioon
def matemaatilised_arvutused(a, b):
    if b == 0:
        raise ValueError("Jagamine nulliga pole lubatud")
    
    summa = a + b
    vahe = a - b
    jagatis = a // b
    korrutis = a * b

    return summa, vahe, jagatis, korrutis

# Ühiktestide klass
class TestMatemaatilisedArvutused(unittest.TestCase):
    
    def test_matemaatilised_arvutused(self):
        # Test õigete väärtuste jaoks
        self.assertEqual(matemaatilised_arvutused(10, 5), (15, 5, 2, 50))
        self.assertEqual(matemaatilised_arvutused(0, 1), (1, -1, 0, 0))
        self.assertEqual(matemaatilised_arvutused(7, 3), (10, 4, 2, 21))
    
    def test_jagamine_nulliga(self):
        # Test jagamist nulliga
        with self.assertRaises(ValueError):
            matemaatilised_arvutused(10, 0)

if __name__ == '__main__':
    unittest.main()
