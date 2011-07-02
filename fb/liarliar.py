#!/usr/bin/env python
import sys
import re

def liar(f):
	fs = open(f)
	n = int(fs.readline().strip())
	accuse = {}
	truthtab = {}
	count = 0
	lastm = 0
	curm = ''
	#Assuming one word names! Count can be ignored.
	for l in fs:
		t = re.split('[ \t]*', l)
		accuser = t[0].rsplit('\n')[0]
		if len(t) == 2:
			#curm = int(t[1])
			curacc = accuser #current accuser
		else:
			ex = []
			ex = accuse.setdefault(curacc, ex)
			ex.append(accuser)

	for k, v in accuse.items():
#		print "processing" , k
		val = truthtab.setdefault(k, "T")
		accused = accuse[k]
		for acc in accused:
			try:
				accusedval = truthtab[acc]
				if accusedval == "T":
					truthtab[k] = "F"
				else:
					truthtab[k] = "T"
				break
			except KeyError:
				pass
#		print "val is", val
		
#	print accuse
#	print truthtab
	f = 0
	t = 0
	for k,v in truthtab.items():
		if v == "F":
			f += 1
		else:
			t +=1

	print max(f, t), min(f,t)
	fs.close()

def main():
	liar(sys.argv[1])

if __name__ == '__main__':
	main()
