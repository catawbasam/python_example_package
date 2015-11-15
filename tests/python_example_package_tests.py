from nose.tools import *
import python_example_package

def setup():
    print "SETUP!"

def teardown():
    print "TEAR DOWN!"

def test_basic():
    print "I RAN!"
    
def test_add():
    assert_equal( python_example_package.add(1,2),  3)
    assert_equal( python_example_package.add(0,0),  0)
    assert_equal( python_example_package.add(-1,-1),  -2)