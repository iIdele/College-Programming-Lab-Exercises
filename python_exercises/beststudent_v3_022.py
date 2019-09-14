import sys
def grades(l):
	mark = l.split()
	grade = int(mark[0])
	name = ' '.join(mark[1:len(mark)])

	print('Best student:' , name)
	print('Best mark:', grade)

def main():
	s = sys.argv[1]
	all_grades = []
	results = []
	with open (s, 'r') as f:	
		for line in f:
			try:
				all_grades.append(int(line[0:2]))

			except FileNotFoundError:
				print('The file {} could not be opened.'.format(s))

			except ValueError:
				print('Invalid mark {} encountered. Skipping.'.format(line[0:2]))

			finally:
				results.append(line)

		largest = max(results)
		grades(largest)

if __name__ == '__main__':
 	main()