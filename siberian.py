#!/usr/bin/python3

from sys import argv, exit

def main(argc, argv):
	if 'debug' in argv:
		debug = True
	else:
		debug = False
	data = input()
	data_without_space = data.replace(' ', '')
	size = len(data_without_space)
	blocks = []
	if 'mixin' in argv:
		from math import sqrt
		max_line = int(sqrt(size * 2)) + 1
		right_line = (max_line - 1) * max_line // 2
		if right_line > size:
			max_line -= 1
			right_line -= max_line

		double_line = size - right_line
		rd = 0
		print(max_line, right_line, double_line)
		i = max_line - 1
		while i > 0:
			blocks.append(
			data_without_space[rd:rd + i]
			)
			rd += i
			if i == double_line:
				blocks.append(
				data_without_space[rd:rd + i]
				)
			i -= 1
	else:
		blocks = data.split()
	print(' '.join(blocks))
	index = 0
	block = 0
	num = 0
	direction = 1
	answer = ''
	length = len(blocks)
	end = False
	while index < length and len(answer) < size:
		if direction == 1:
			block = index
			num = 0
		elif direction == -1:
			block = 0
			num = index

		for _ in range(index):
			if debug:
				print(block, num)
			try:
				answer += blocks[block][num]
			except IndexError:
				end = True
				break
			block -= direction
			num += direction
		if end:
			break
		
		direction *= -1
		try:
			answer += blocks[block][num]
		except IndexError:
			break
		index += 1
	print(answer)
	return 0

if __name__ == '__main__':
	exit(main(len(argv), argv))
