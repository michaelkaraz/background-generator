import unittest
import testcase

class TestMain(unittest.TestCase):
    def test_add(self):
        test_p1 = 10
        result = testcase.add(test_p1)
        self.assertEqual(result,15)

    def test_add2(self):
        test_p1 = "sdfds"
        result = testcase.add(test_p1)
        self.assertIsInstance(result,ValueError)

unittest.main()