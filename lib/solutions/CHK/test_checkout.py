import unittest
import checkout_solutions

class TestCheckout(unittest.TestCase):

    def test_checkout(self):
        self.assertEqual(checkout_solutions.chechout("AABBEE"),195)
if __name__ == "__main__":
    unittest.main()