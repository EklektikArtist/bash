import sys

file_name = sys.argv[1]
repass = True
lines = []

def prints_list(lists):
    for l in lists:
        print l,

def itt():
    global repass
    global lines
    repass = False
    prev_line = ""
    i = 0
    for line in lines:
        if "./" in line:
            if "./" in prev_line:
                del lines[(i-1)]
                repass = True
                break
        prev_line = line
        i+=1



with open(file_name) as f:
    for line in f:
        lines.append(line)
    while repass:
        itt()
    if "./" in lines[len(lines)-1]:
        del lines[len(lines)-1]

prints_list (lines)
