# Exercise: Predict what double("22") will do, then run and check.
 
# Prediction:
# double("22") will return "2222".
# Because Python's * operator on a string repeats it, not multiplies it mathematically.
# So "22" * 2 = "2222", not 44.
 
def double(value):
    return value * 2
 
print(double(22))    
print(double("22"))  