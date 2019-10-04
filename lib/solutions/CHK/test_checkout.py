import unittest
import checkout_solution

class TestCheckout(unittest.TestCase):

    def test_checkout(self):
        self.assertEqual(checkout_solution.checkout("AABBEE"),210)
        self.assertEqual(checkout_solution.checkout("AAAAAA"),250)
        self.assertEqual(checkout_solution.checkout("EEEEBB"),160)
        self.assertEqual(checkout_solution.checkout("BEBEEE"),160)
        self.assertEqual(checkout_solution.checkout("BEBEEEFFF"),180)
        self.assertEqual(checkout_solution.checkout("ABCDEABCDE"),280)
        self.assertEqual(checkout_solution.checkout("FFFFFFF"),50)
    
    def test_apply_freebees(self):
        self.assertEqual(checkout_solution.apply_freebees("FFF"),"FF")
        self.assertEqual(checkout_solution.apply_freebees("BEBEEEFFF"),"EEEEFF")
        self.assertEqual(checkout_solution.apply_freebees("RRRQ"),"RRR")
        self.assertEqual(checkout_solution.apply_freebees("MNNNM"),"NNNM")

if __name__ == "__main__":
    unittest.main()