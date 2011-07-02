import sys

def hop(f):
	fs = open(f)
	n = int(fs.readline().strip())
	for i in range(1, n + 1):
		if i % 3 == 0:
			if i % 5 == 0:
				print "Hop"
			else:
				print "Hoppity"
		else:
			print "Hophop"
	fs.close()

def main():
	hop(sys.argv[1])

if __name__ == '__main__':
	main()
