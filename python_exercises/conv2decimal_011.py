import sys
def conv2decimal(s):
	(left, right) = s.strip().split()
	left = left[::-1]
	decinum = 0

	i = 0
	while i < len(left):
		decinum = decinum + (int(left[i]) * (int(right) ** i))
		i = i + 1

	return decinum
    	
def main():
    for line in sys.stdin:
        print(conv2decimal(line))
        

if __name__ == '__main__':
    main()