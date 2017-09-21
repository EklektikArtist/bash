import sys, os
inputfile = open(sys.argv[1])
osrow, oscol = os.popen('stty size', 'r').read().split()
osrow = int(float(osrow)/5)
oscol = int(float(oscol)/3.3)
print ("The input file is '%s'" % sys.argv[1])

def main():
	for line in inputfile.readlines():
		list = []
		line = line.strip('\n')
		print line
		print "Format this line as:"
		list.append(("Title  ", fTitle(line)))
		list.append(("Section", fSection(line)))
		printList(list)
		blankRestOfScreen(4)

def blankRestOfScreen(linesUsed):
	for count in range(oscol - linesUsed - 1):
		print '\r\n'

def printList(list):
	i=0
	for item in list:
		print "%7s:  \"%s\"" % (item[0], item[1])
def fTitle(line):
	return line.upper()

def fSection(line):
	return "	  - " + line

main()
