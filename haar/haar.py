import sys
from math import log,fabs

def haar(args):
	ga = average(args) #global average
	print "Global average", ga
	steps = int(log(len(args), 2))
	
	print "Steps required", steps

	r = len(args)
	res = process(args, r)
	r = r/2
	for i in range(steps - 1):
		print i
		res = process(res, r)
		r = r/2
	return res

def process(args, r):
	res = []
	for i in range(0, r, 2):
		res.append(av(args[i], args[i + 1]))

	j = 0
	for i in range(0, r, 2):
		res.append(args[i] - res[j])
		j += 1

	if r == len(args):
		return res
	else:
		return res + args[r:]

def average(nums):
	sum = 0;
	for i in nums:
		sum += i
	return sum / (len(nums) * 1.0)

def av(i, j):
	return (i+j)/2.0 #http://python-history.blogspot.com/2009/03/problem-with-integer-division.html

def main():
	args = [int(i) for i in sys.argv[1:]]
	if len(args) % 2 != 0:
		print "Odd # of args", len(args)
		return
	res = haar(args)
	print(res)

if __name__ == '__main__':
	main()
