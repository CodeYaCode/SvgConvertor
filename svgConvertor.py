# svgConvertor.py

#author LiuChen

import re
import os
import sys

# source
# file = open('user.svg', encoding='utf-8')
#color
# co = open('color.txt', encoding='utf-8')
# color = co.readline()
# output
# out = open(color+'.svg', 'w', encoding='utf-8')
# outCode = open(color+'.txt', 'w', encoding='utf-8')
# SvgConvertor(file)

# read file
def readDropFile():
	filename = sys.argv[1]
	if filename.split('.')[-1] != 'svg':
		print('Error file formate.')
	try :
		file = open(filename, encoding='utf-8')
		simpleFilename = filename.split(os.path.sep)[-1]
		return (simpleFilename, file)
	except:
		print('Open SVG file fail.')

# read config
def config():
	config = open('config.txt', encoding='utf-8')
	conf = {}
	for line in config:
		strs = line.split('=')
		conf[strs[0]] = strs[1].replace('\n', '')
	return conf

def outFilename(filename, conf, formate):
	# make direction
	filename = filename.split('.')[0]
	path = filename
	if os.path.exists(path):
		pass
	else:
		os.mkdir(path)
	color = conf['color']
	width = conf['width']
	height= conf['height']
	name = filename + '_' + color + "_" + width + 'X' + height + '.' + formate
	return path + os.path.sep + name

# convertor
def SvgConvertor(file=None, simpleFilename=''):
	# read config
	conf = config()
	color = conf['color']
	width = conf['width']
	height= conf['height']
	filename = conf['filename']
	# source file
	file = open(filename, 'r', encoding='utf-8')
	# out file 
	outSvg = open(outFilename(filename, conf, 'svg'), 'w', encoding='utf-8')
	outCode = open(outFilename(filename, conf, 'txt'), 'w', encoding='utf-8')
	regColor = r'fill="#\w+"'
	regWidth = r'width="\w+\.*\w+"'
	regHeight= r'height="\w+\.*\w+"'
	patternC = re.compile(regColor)
	patternW = re.compile(regWidth)
	patternH = re.compile(regHeight)
	for line in file.readlines():
		if patternC.findall(line):
			line, index = re.subn(regColor, 'fill="' + color + '"', line)
		if patternW.findall(line):
			line, index = re.subn(regWidth, 'width="' + width + 'px"', line)
		if patternH.findall(line):
			line, index = re.subn(regHeight, 'height="' + height + 'px"', line)

		outSvg.write(line)
		outCode.write(line)

#main
def main():
	# simpleFilename, file = readDropFile()
	# file = open('C:\\Users\\liuchen\\Desktop\\SvgConvertor\\user.svg', encoding='utf-8')
	# simpleFilename = file.name.split(os.path.sep)[-1]
	# print(simpleFilename)
	# input()
	# print(simpleFilename + " CONVERT [START]")
	SvgConvertor()
	# print(simpleFilename + ' CONVERT [FINISH]')

## main ##
main()
print('Convert finish!')
print('Press any key...')
input()