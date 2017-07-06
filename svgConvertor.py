# svgConvertor.py

#author LiuChen

import re

# source
file = open('user.svg', encoding='utf-8')
#color
co = open('color.txt', encoding='utf-8')
color = co.readline()
# output
out = open(color+'.svg', 'w', encoding='utf-8')
outCode = open(color+'.txt', 'w', encoding='utf-8')
SvgConvertor(file)


def SvgConvertor(file):
	reg = r'#\w+'
	pattern = re.compile(reg)
	for line in file.readlines():
		if pattern.findall(line):
			s, index = re.subn(reg, color, line)
			out.write(s)
			outCode.write(s)
		else :
			out.write(line)
			outCode.write(line)