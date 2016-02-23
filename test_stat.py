from nose.tools import assert_equal, assert_raises

from stats import mean

def test_mean_1():
    
    obs = mean([1,2,3])
    exp = 2
    assert_equal(obs, exp)

def test_mean_2():
    
    obs = mean([3,4,5])
    exp = 4
    assert_equal(obs, exp)

def test_mean_float():
    
    obs = mean([3,4])
    exp = 3.5
    assert_equal(obs, exp)

def test_mean_empty():
    
    obs = mean([])
    exp = None
    assert_equal(obs, exp)

def test_mean_3():
    
    obs = mean([-3,-4,-5])
    exp = -4
    assert_equal(obs, exp)

def test_mean_4():
    
    obs = mean([4])
    exp = 4
    assert_equal(obs, exp)

def test_mean_5():
    
    obs = mean(5)
    exp = 5
    assert_equal(obs, exp)

def test_mean_string():
    
    assert_raises(TypeError, mean, ['one', 'two'])
