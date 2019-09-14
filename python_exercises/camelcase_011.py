import sys
def camelcase(s):
	s = s.strip().split()

	i = 0
	while i < len(s):
		s[i] = s[i].capitalize()
		i = i + 1

	return " ".join(s)
    	
def main():
    for line in sys.stdin:
        print(camelcase(line))
        

if __name__ == '__main__':
    main()