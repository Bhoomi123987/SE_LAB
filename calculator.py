def validate_numbers(a, b): 
"""Ensure inputs are numeric before performing operations.""" 
if not isinstance(a, (int, float)) or not isinstance(b, (int, float)): 
raise ValueError("Inputs must be numbers") 
return a, b 
def add(a, b): 
a, b = validate_numbers(a, b) 
return a + b 
def subtract(a, b): 
a, b = validate_numbers(a, b) 
return a - b 
def multiply(a, b): 
a, b = validate_numbers(a, b) 
return a * b