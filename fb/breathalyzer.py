#!/usr/bin/env python
import sys

def breathalyze(f):
	fw = open("/var/tmp/twl06.txt")
	words = fw.readlines()
	print len(words)
	fw.close()
	
	#inputwords = []
	count = 0
	
	inp = open(f)
	for f in inp:
		t = f.rsplit("\n")[0].split()
		for tok in t:
			w = tok.strip().upper()
			changes = diff(words, w)
			if changes > 0:
				count += changes

#	print inputwords

	print count
	inp.close()

def diff(words, w):
	pass

def levenshtein(w1, w2):
	'''
	From the wikipedia article
	'''
	l1 = len(w1)
	l2 = len(w2)
	res = [[0 for i in xrange(l2 + 1)] for j in xrange(l1 + 1)] #init zeroed matrix
	print res

	for i in xrange(l1 + 1):
		res[i][0] = i
	for i in xrange(l2 + 1):
		res[0][i] = i
	print_matrix(res)

	for j in xrange(0, l2):
		for i in xrange(0, l1):
#			print "i", i
#			print "j", j
			if w1[i] == w2[j]:
				res[i][j] = res[i - 1][j - 1]
			else:
				res[i][j] = get_min(res[i - 1][j] + 1, res[i][j - 1] + 1, res[i - 1][j - 1] + 1)

	print "Post op"
	print_matrix(res)
	return res[l1 - 1][l2 - 1]

def print_matrix(res):
	for j in xrange(len(res)):
		print ""
		for i in xrange(len(res[j])):
			print res[j][i],


def get_min(a, b, c):
	return min(min(a,b), c)

def main():
	r = levenshtein('kitten', 'sittin')
	print "Result", r
	#breathalyze(sys.argv[1])

if __name__ == '__main__':
	main()
