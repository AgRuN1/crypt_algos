#!/usr/bin/python3

from sys import exit, stderr, argv

def main():
	string = input()
	string = string.replace(' ', '')
	length = len(string)
	if length % 15 != 0:
		print('Incorrect code', file=stderr)
		return 1
	data = []
	for i in range(0, length, 15):
		current_elem = string[i:i+15]
		data.append(current_elem)
	numbers = []
	for block in data:
		code = ''
		r = []
		for _ in range(4):
			r.append('')
		for i in range(0, 15, 2):
				r[0] += '{} '.format(block[i])
		for i in range(1, 15, 4):
			r[1] += '{} {} '.format(block[i], block[i+1])
		for i in range(3, 15, 8):
			for j in range(4):
				r[2] += '{} '.format(block[i+j])
		for i in range(7, 15, 16):
			for j in range(8):
				r[3] += '{} '.format(block[i+j])
		result = ''
		for i in r[::-1]:
			result += str(sum([int(j) for j in i.split()]) % 2)
		numbers.append(int(result, 2))
	for i in range(len(data)):
		num = numbers[i]
		if num != 0:
			current_value = data[i][num - 1]
			if current_value == '1':
				current_value = '0'
			else:
				current_value = '1'
			data[i] = data[i][:num-1] + current_value + data[i][num:]
		data[i] = ''.join([data[i][j] for j in range(len(data[i])) if j!=0 and j!=1 and j!=3 and j!=7])
	print(' '.join(data))

if __name__ == '__main__':
	exit(main())
