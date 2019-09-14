import sys
def diamond(x):
	i = 1
	while i < x + 1:
		diamond = (' ' * (x - i) + '* ' * i).rstrip()
		print(diamond)
		i = i + 1

	i = i - 2

	while 0 < i:
		diamond = (' ' * (x - i) + '* ' * i).rstrip()
		print(diamond)
		i = i + 1

def main():
	diamond(int(sys.argv[1]))

if __name__ == '__main__':
	main()
