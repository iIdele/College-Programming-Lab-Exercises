import sys
def make_dic():
	contacts = {}
	names = []
	numbers = []
	emails = []
	file = sys.argv[1]
	with open (file , 'r') as f:
		for line in f:
			(name,number,email) = line.split()
			names.append(name)
			numbers.append(number)
			emails.append(email)
	
	i = 0
	while i < len(names):
		contacts[names[i]] = numbers[i], emails[i]
		i = i + 1
	
	return contacts
	
def main():
	dic = make_dic()
	for line in sys.stdin:
		k = line.strip()
		if k in dic:
			print('Name: {}'.format(k))
			print('Phone: {}'.format(dic[k][0]))
			print('Email: {}'.format(dic[k][1]))
		else:
			print('Name: {}'.format(k))
			print('No such contact')

if __name__ == '__main__':
	main()
		