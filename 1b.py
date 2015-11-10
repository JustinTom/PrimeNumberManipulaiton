#!/usr/bin/python
import time

#Uses the iterative method to calculate the d.
def findD(e, tt):
	#Start with 1 multiplication value
	i = 1
	while True:
		#Main formula we need to calculate it the d.
		tempResult = i*tt+1
		#Check if the new value is divisible by the e value.
		if (tempResult%e) == 0:
			#Return the value if it is divisible.
			return tempResult/e
		else:
			#If it is not the correct number, increase value by 1 and try again.
			i+=1
			continue

def main():
	eValue = int(input("What is the e value? "))
	tt = int(input("What is the totient value? "))
	start = time.clock()
	dValue = findD(eValue, tt)
	end = time.clock()
	elapsed = (end - start)
	print "From e value: %d & totient value: %d, the d value is: %d" %(eValue, tt, dValue)
	print "Total time taken to calculate: %f seconds" %elapsed

if __name__ == '__main__':
	main()