import sys
import Image
import haar as h

def apply(infile, outfile):
	im = Image.open(infile)
	pixels = list(im.getdata())
	print "Olength", len(pixels)
	#print "Orig", pixels
	res = h.haar(pixels)

	print "Tlen", len(res)
	print "Tav", res[0]
	#print "Trans", res
	im.putdata(res)
	im.save(outfile)


def main():
	apply(sys.argv[1], sys.argv[2])

if __name__ == '__main__':
	main()
