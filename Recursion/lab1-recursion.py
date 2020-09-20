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

if __name__ == '__main__':
	print(sum1ToN(7))