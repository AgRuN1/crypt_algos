#!/usr/bin/python3

from sys import exit

def main():
	data = input()
	data = data.replace(' ', '')
	first, *data = data
	blocks = []
	block_len = 0
	readed = False
	current_value = ''
	for i in data:
		if not(readed) and i == '1':
			readed = True
		if readed:
			current_value += i
			if block_len == 0:
				blocks.append(current_value)
				current_value = ''
				readed = False
			else:
				block_len -= 1

		else:
			block_len += 1

	result = ''
	for block in blocks:
		result += first * int(block, 2)
		first = '0' if first == '1' else '1'

	print(result)
	return 0;

if __name__ == '__main__':
	exit(main())
