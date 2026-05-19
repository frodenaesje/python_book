import unittest

class TestMath(unittest.TestCase):
    def test_simple(self):
        with self.subTest(msg="Test addition"):
            self.assertEqual(2 + 2, 5)
        with self.subTest(msg="Test multiplication"):
            self.assertEqual(3 * 3, 8)
        with self.subTest(msg="Test subtraction"):
            self.assertEqual(5 - 2, 4)

if __name__ == "__main__":
    unittest.main()
