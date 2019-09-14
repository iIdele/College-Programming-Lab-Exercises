import sys
def contains(s):
	(left, right) = s.strip().split()
	tally = []

	i = 0
	while i < len(left):
		tally.append(left[i].lower() in right.lower())
		right = right.replace(left[i], '')
		i = i + 1

	if False in tally:
		print('False')
	else:
		print('True')
    	

    	
def main():
    for line in sys.stdin:
        contains(line)

if __name__ == '__main__':
    main()