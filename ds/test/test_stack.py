import unittest

class TestSum(unittest.TestCase):

    def TestSum(self):
        self.assertEqual([1,2,3],6,'Should be equal to 6')
        
    def test_sum_tuple(self):
        self.assertEqual((1,2,2),6,'Should be equal to 6')
        
        
if __name__ == '__main__':
    unittest.main()