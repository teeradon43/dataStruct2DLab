"""
	Lab1 - Recursion
"""

def fac(n): # return n!
	if n == 1:
		return 1
	else:
		return fac(n-1) * n

def sum1ToN(n): # return sum of 1 -> n while n >= 1
	if n == 1:
		return n
	else:
		if n < 1 :
			return 'Error'
		else:
			return sum1ToN(n-1)+n

def printNto1(n): #print number n to 1
	if n == 1:
		print(n)
	else:
		print(n)
		return printNto1(n-1)

if __name__ == '__main__':
	printNto1(7)