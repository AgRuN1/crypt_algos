#!/usr/bin/python3

from sys import exit, stderr
from math import ceil

def main():
	data = input("Data: \n")
	key = input("Key: ")
	columns = len(key)
	length = len(data)
	if columns > length:
		print('Incorrect key', file=stderr)
		return 1
	rows = ceil(length / columns)
	blocks = []
	for i in range(0, length, rows):
		current_elem = data[i:i+rows]
		blocks.append(current_elem)
	result = ''
	print(blocks)
	for row in range(rows):	
		for num in key:
			try:
				result += blocks[int(num) - 1][row]
			except(IndexError):
				break
	print(result)

if __name__ == '__main__':
	exit(main())
