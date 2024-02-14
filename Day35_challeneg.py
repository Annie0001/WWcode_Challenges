# Write a simple unit test for a function that adds two numbers


import unittest

def add_two_numbers(a,b):
    sum = 0
    sum = a + b
    return sum

class TestStringMethods(unittest.TestCase):

    def test_add_two_numbers(self):
        self.assertEqual(add_two_numbers(2,3), 5)

    def test_add_two_numbers_false(self):
        self.assertNotEqual(add_two_numbers(2,3), 6)




if __name__ == '__main__':
    unittest.main()

