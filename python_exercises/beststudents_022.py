import sys
def grades(l):
	names = (', '.join(l)[4:])
	grade = (l[0][0:2])

	print('Best student(s):' , names)
	print('Best mark:', grade)

def main():
	s = sys.argv[1]
	all_grades = []
	results = []
	best = []
	try:
		with open (s, 'r') as f:	
			for line in f:
				try:
					all_grades.append(int(line[0:2]))

				except ValueError:
					print('Invalid mark {} encountered. Skipping.'.format(line[0:2]))

				finally:
					results.append(line)

		sorted_results = sorted(results)
		highscorer = sorted_results[-1].strip()
		score = highscorer[0:2]
		best.append(score)
		for result in results:
			if (result[0:2]) == score:
				best.append(result[3:].strip())

		grades(best)
	except FileNotFoundError:
		print('The file {} could not be opened.'.format(s))
				
if __name__ == '__main__':
 	main()