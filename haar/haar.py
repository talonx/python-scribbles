import sys
from math import log

def haar(args):
	args = [int(i) for i in args[1:]]
	l = len(args)
	if l == 0 or l % 2 != 0:
		print "Even number of args required:", len(args)
		return
	
	ga = average(args) #global average

	steps = int(log(l, 2))
	print "Steps required", steps

	res = process(args)

	for i in range(steps - 1):
		res = process(res)

	print res

def process(args):
	res = []
	for i in range(0, len(args), 2):
		res.append(av(args[i], args[i + 1]))

	j = 0
	for i in range(0, len(args), 2):
		res.append(args[i] - res[j])
		j += 1

	return res

def average(nums):
	sum = 0;
	for i in nums:
		sum += i
	return sum / (len(nums) * 1.0)

def av(i, j):
	return (i+j)/2.0 #http://python-history.blogspot.com/2009/03/problem-with-integer-division.html

def main():
	haar(sys.argv)

if __name__ == '__main__':
	main()
