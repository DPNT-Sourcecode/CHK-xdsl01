import unittest
import checkout_solution

class TestCheckout(unittest.TestCase):

    def test_checkout(self):
        self.assertEqual(checkout_solution.checkout("AABBEE"),195)
        self.assertEqual(checkout_solution.checkout("ABCDEGX"),-1)
        self.assertEqual(checkout_solution.checkout("AAAAAA"),250)
if __name__ == "__main__":
    unittest.main()