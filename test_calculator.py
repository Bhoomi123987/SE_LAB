import pytest 
from calculator import add, subtract, multiply 
def test_add(): 
assert add(2, 3) == 5 
assert add(-1, 1) == 0 
assert add(2.5, 3.5) == 6.0 
def test_subtract(): 
assert subtract(5, 2) == 3 
assert subtract(0, 3) == -3 
def test_multiply(): 
assert multiply(2, 3) == 6 
assert multiply(-1, 4) == -4 
def test_invalid_inputs(): 
with pytest.raises(ValueError): 
add("a", 2) 
with pytest.raises(ValueError): 
subtract(1, "b") 
with pytest.raises(ValueError): 
multiply("x", "y")