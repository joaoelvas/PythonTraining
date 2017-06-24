l = [1, 1, 1, 1, 2, 1, 1, 1, 1]

print(l)

while 1:
	try:
		l.remove(1)
	except ValueError:
		break

print(l)