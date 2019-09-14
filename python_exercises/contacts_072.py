class Contact(object):
	
	def __init__(self, name, phone, email):
		self.name = name
		self.phone = phone
		self.email = email
		
	def __str__(self):
		return '{} {} {}'.format(self.name, self.phone, self.email)
	

class ContactList(object):
	
	def __init__(self, d={}):
		self.d = d
	
	def add_contact(self, contact):
		self.d[contact.name] = contact
		
	def del_contact(self, key):
		if key in self.d:
			del self.d[key]
	
	def get_contact(self, key):
		if key in self.d:
			return self.d[key]
		else:
			return '{} : No such contact'.format(key)
		
	def __str__(self):
		string = 'Contact list\n------------'
		for k in sorted(self.d.keys()):
			string += '\n{}'.format(self.d[k])
		
		return string