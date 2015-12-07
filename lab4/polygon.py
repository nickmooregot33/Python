#!/software/SciPy-Stack-2.7.10-x86_64/bin/python2

from math import tan, pi

def a(n,s):
     return s/(2 * tan(pi/n))
 
def area_polygon(n, s=1.0):
     if n <= 2:
             return 0.0
     return .5 * n * s * a(n,s)

if area_polygon(3) == 0.43301270189221946:
	print "True"
if area_polygon(7) == 3.6339124440015893:
	print "True"
if area_polygon(2) == 0.0:
	print "True"
