print "QUADRATIC SOLVER"
print "ax^2 + bx + c = 0"
a_str=raw_input("Please enter a:")
b_str=raw_input("Please enter b:")
c_str=raw_input("Please enter c:")

a=float(a_str)
b=float(b_str)
c=float(c_str)

square_root=(b**2-4*a*c)**.5
denominator = 2*a
 
answer1=(-b + square_root)/ denominator
answer2=(-b - square_root)/ denominator
print "solution 1: %f" %answer1
print "solution 2: %f" %answer2
