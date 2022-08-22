from sympy import * 
x = symbols('x')
expr = (x**2+2*x+1)/(x+1)   #you can try with different expressions
  
print("Before Simplification : {}".format(expr))
    
# Use sympy.simplify() method
smpl = simplify(expr) 
    
print("After Simplification : {}".format(smpl))
