class Contact(object):

	def __init__(self, name, phone, email):
		self.name = name
		self.phone = phone
		self.email = email

	def __str__(self):
		return 'Name: {}\nPhone: {}\nEmail: {}'.format(self.name, self.phone, self.email)

class ContactList(object):

	def __init__(self):
		self.dic = {}

	def add(self, contact):
		if contact.name in self.dic:
			print('Contact already present')
		else:
			self.dic[contact.name] = contact.phone, contact.email

	def remove(self, name):
		if name in self.dic:
			del self.dic[name]
		else:
			print('No such Contact')

	def display(self, name):
		if name in self.dic:
			print ('Name: {}\nPhone: {}\nEmail: {}'.format(name, self.dic[name][0], self.dic[name][1]))
		else:
			print('No such contact')

	def __str__(self):
		for (k,v) in sorted(self.dic.items()):
			print('Name: {}\nPhone: {}\nEmail: {}'.format(k, v[0], v[1]))
		return 'Contacts: {}'.format(len(self.dic))

def main():
	cl = ContactList()

	c1 = Contact(name='Max', phone='087 2233456', email='max@google.com')

	c2 = Contact(name='John', phone='087 2253486', email='john@google.com')

	cl.add(c1)
	cl.add(c2)
	print(cl)


if __name__ == '__main__':
	main()