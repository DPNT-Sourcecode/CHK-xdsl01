import unittest
import checkout_solution

class TestCheckout(unittest.TestCase):

    def test_checkout(self):
        self.assertEqual(checkout_solution.checkout("AABBEE"),195)
        self.assertEqual(checkout_solution.checkout("ABCDEGX"),-1)
        self.assertEqual(checkout_solution.checkout("AAAAAA"),250)
        self.assertEqual(checkout_solution.checkout("EEEEBB"),160)
        self.assertEqual(checkout_solution.checkout("BEBEEE"),160)

if __name__ == "__main__":
    unittest.main()