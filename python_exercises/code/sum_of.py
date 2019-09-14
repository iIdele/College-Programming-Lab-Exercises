def sum_of(l):
	total = 0
	i = 0
	while i < len(l):
		total = total + l[i]
		i += 1
	return total

print(sum_of([1,2,3,4,5]))
