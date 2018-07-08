#!/usr/bin/python3

import sys

if len(sys.argv) < 2:
	data = input()
else:
	file_name = sys.argv[1]
	f = open(file_name, 'r')
	data = f.read().replace('\n', '')
data = data.replace(' ', '')
length = len(data)
for i in range(0, length, 8):
	num = data[i : i + 8]
	print(int(num, 2), end=' ')
print('\nReaded:', length / 8, 'bytes')
