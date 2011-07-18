#!/usr/bin/env python
import sys
import re

def breathalyze(f):
	words = load(f)
	count = 0
	inp = open(f)
	for f in inp:
		t = f.rsplit("\n")[0].split()
		for tok in t:
			w = tok.strip().upper()
			changes = diff(words, w)
			if changes > 0:
				count += changes

	inp.close()
	return count

def load(f):
	words = {}
	fw = open("/var/tmp/twl06.txt")
	curlet = ''
	curlist = []
	for w in fw:
		w = re.split('\r\n', w)[0]
		fl = w[0]
		if curlet != fl:
			curlet = fl
			curlist = words.setdefault(curlet, [])
		curlist.append(w)

	#print len(words)
	#print words.keys()
	fw.close()
	return words

def diff(words, tomatch):
	try:
		list = words[tomatch[0]]
		#list = ['IAMBICS']
		#print list
		if tomatch in list:
			#print "exact match", tomatch
			return 0
		
		score = 0
		matched = ''
		for word in list:
			d = levenshtein(word, tomatch)
			#print "leven for %s is %d" % (word, d)
			if score == 0 or d < score:
				score = d
				matched = word
		
		#print "Score for %s is %d match %s" % (tomatch, score, matched)
		return score
	except KeyError:
		"Word does not start with a letter. Skipping", w


def levenshtein(w1, w2):
	'''
	From the wikipedia article
	'''
	l1 = len(w1)
	l2 = len(w2)
	res = [[0 for i in xrange(l2 + 1)] for j in xrange(l1 + 1)] #init zeroed matrix
	#print res

	for i in xrange(l1 + 1):
		res[i][0] = i
	for i in xrange(l2 + 1):
		res[0][i] = i
	#print_matrix(res)

	for i in xrange(1, l1 + 1):
		for j in xrange(1, l2 + 1):
			res[i][j] = get_min(res[i - 1][j] + 1, res[i][j - 1] + 1, res[i - 1][j - 1] + (0 if w1[i - 1] == w2[j - 1] else 1))

	#print "Post op"
	#print_matrix(res)
	return res[l1][l2]

def print_matrix(res):
	for j in xrange(len(res)):
		print ""
		for i in xrange(len(res[j])):
			print res[j][i],
	print ""


def get_min(a, b, c):
	return min(min(a,b), c)

def main():
	#r = levenshtein('goud', 'good')
	#print r
	#r = levenshtein('a', 'b')
	#print r
	#print "Result", r
	print breathalyze(sys.argv[1])

if __name__ == '__main__':
	main()
