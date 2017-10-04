import sys, os
inputfile = open(sys.argv[1])
outputfile = open(sys.argv[2], "w")
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
		list.append(("Title   ", fTitle(line)))
		list.append(("Section ", fSection(line)))
		list.append(("Sub Pt 1", fSub1(line)))
		list.append(("Sub Pt 2", fSub2(line)))
		list.append(("Sub Pt 3", fSub3(line)))
		printList(list)
		selection = input("Selected option: ")
		outputfile.write(str(list[selection]))
		#blankRestOfScreen(4)

def blankRestOfScreen(linesUsed):
	for count in range(oscol - linesUsed - 1):
		print '\r\n'

def printList(list):
	i=0
	for item in list:
		print "%d) %8s:  \"%s\"" % (i, item[0], item[1])
		i=i+1
def fTitle(line):
	return line.upper()

def fSection(line):
	return "	" + line

def fSub1(line):
	return "	  - " + line

def fSub2(line):
	return "	      - " + line

def fSub3(line):
	return "	         (" + line +')'

main()
