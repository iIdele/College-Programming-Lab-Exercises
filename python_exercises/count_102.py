def count_letters(s):
	if len(s) == 0:
		return 0
	
	return 1 + count_letters(s[:-1])

def main():
	len = None
	print(count_letters('cat'))
	print(count_letters('catastrophe'))
	print(count_letters(''))

if __name__ == '__main__':
	main()