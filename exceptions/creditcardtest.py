import unittest
from creditcardexample import *


class cardvalidationtest(unittest.TestCase):
    def setUp(self):
        print("setup")

    def test_validatecard_valid(self):
        result = cardvalidation(date(2021, 8, 8))
        self.assertEqual("valid", result)

    def test_validatecard_invalid(self):
        result = cardvalidation(date(2020, 8, 8))
        self.assertEqual("expired", result)

    def tearDown(self):
        print("teardown")


if __name__ == '__main__':
    unittest.main()
