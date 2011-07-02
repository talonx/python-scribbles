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
	

def main():
	breathalyze(sys.argv[1])

if __name__ == '__main__':
	main()
