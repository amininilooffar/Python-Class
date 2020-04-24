Python 3.7.6 (tags/v3.7.6:43364a7ae0, Dec 19 2019, 00:42:30) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> class coordinate:
	x=0
	y=0

	
>>> p1= coordinate()
>>> p2= coordinate()
>>> 
>>> def distantpoint (point1, point2):
	return ((point1.x-point2.x)**2+ (point1.y- point2.y)**2)**0.5

>>> p1.x=5
>>> p2.x=6
>>> p1.y=8
>>> p2.y=12
>>> distantpoint (p1, p2)
4.123105625617661
>>> 