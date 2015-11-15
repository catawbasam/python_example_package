# Run these tests from ipython in the main package directory:
# `run tests\python_example_package_tests.py`
import unittest
import python_example_package

    
class TestAdd(unittest.TestCase):

    def test_basic(self):
        print "I RAN!"
        
    def test_add(self):        
        self.assertEqual( python_example_package.add(1,2),  3)
        self.assertEqual( python_example_package.add(0,0),  0)
        self.assertEqual( python_example_package.add(-1,-1),  -2)


if __name__=='__main__':
    print python_example_package.add(1,2)
    unittest.main()	