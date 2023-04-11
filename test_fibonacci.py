import unittest

def fibonacci(number):
    if number <= 1:
        return number
    return fibonacci(number - 2) + fibonacci(number)

class TestFibonacci(unittest.TestCase):
    def test_1(self):
       self.assertEqual(1, fibonacci(1))
    
    def test_2(self):
       self.assertEqual(1, fibonacci(2))

    def test_3(self):
       self.assertEqual(2, fibonacci(3))

    def test_4(self):
       self.assertEqual(3, fibonacci(4))

    def test_5(self):
       self.assertEqual(5, fibonacci(5))

    def test_6(self):
        self.assertEqual(8, fibonacci(6))

    def test_7(self):
        self.assertEqual(13, fibonacci(7))

if __name__ == '__main__':
    unittest.main()