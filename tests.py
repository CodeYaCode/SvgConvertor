import sys

file = open(sys.argv[1], encoding='utf-8')
print(file.name.split('\\')[-1])
for line in file:
	print(line)

input()