# #STRINGS

# s = 'Python_programming'
# try:
# 	print(s[-5:-10:-1])
# 	i = len(s) // 3
# 	print(s[:i] + s[i+9:])
# 	s[7] = 'b'
# 	print(s)
# except:
# 	print('We have a problem')


# s = 'Winter is coming.'

# print(s[:len(s):2])
# print(s[-1:-len(s):-1])

# i = (len(s) - 2) // 2
# print(i)
# print(s[:i] + s[i+1:])

# s = 'Summer_holidays'
# try:
# 	print(s[-2:-12:-2])
# 	i = (len(s) // 2)
# 	print(s[i:])
# 	s += '!'
# 	print(s)
# except:
# 	print('We have a problem')

# s = 'Dublin City'
# print(s[3::3z])

# #COMPARISON
# a = [1,2,3]
# b = a[:]

# print(a == b)

# #FORMATTING
# from math import pi
# print(pi)

# print('{:^20f}'.format(pi))
# s = 'apples'
# print('{:^10s}'.format(s))
# a = 6
# b = 2
# x = 7//2
# print('{:^{}.{}f}'.format(x,a,b))

# #LIST COMPREHENSION
# l = [2,1,3,4,5,8]
# sum_of_squares = [num ** 2 for num in l if num % 2 != 0]
# total = 0
# for num in sum_of_squares:
# 	total += num
# print(total)
# #.............................
# def palindrome(s):
# 	reverse = [l for l in s[::-1]]
# 	reverse = ''.join(reverse)
# 	return(s == reverse)
# print(palindrome('level'))
# #..............................
# s = 'This is an example sentence'
# consonants = [l for l in s if l not in 'aeiou ']
# print(len(consonants))
# #...............................
# n = list(range(15))
# sum_of_n = [num ** 2 for num in n]
# total = 0
# for num in sum_of_n:
# 	total += num
# print(total)
# #...........................
# def all_vowels(s):
# 	vowels = 'aeiou'
# 	i = 0
# 	while i < len(vowels) and vowels[i] in s:
# 		i = i + 1
# 	if i < len(vowels):
# 		return False
# 	else:
# 		return True

# w = ['cat', 'audiotape', 'businesswoman','exultation', 'flouridate', 'dog']
# words = [s for s in w if all_vowels(s) == True]
# print(min(words))
# #............................