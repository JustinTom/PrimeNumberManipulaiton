#!/usr/bin/python
from fractions import gcd
import time

#Finds co-prime number through increasing both x and y values (the two coprime values.)
def coprimes(num):
	for x in range (2, num):
		for y in range (2, num):
			#If the GCD of both x and y values aren't 1 (non prime)
			#and if they aren't the same values, check if their product
			#equals the specified number and return it if true.
			while gcd(x,y) == 1 and x != y:
				if (x * y == num):
					return x, y
				else:
					break

def main():
	number = int(input("What is the modulus number? "))
	start = time.clock()
	num1, num2 = coprimes(number)
	end = time.clock()
	elapsed = (end - start)
	print "These are the co prime numbers: %d & %d" %(num1,num2)
	print "Total time taken to calculate: %f seconds" %elapsed

if __name__ == '__main__':
	main()