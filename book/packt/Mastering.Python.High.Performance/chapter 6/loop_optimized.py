

accu = 0
for i in range(1000):
	accu += i

def accuFn(c):
	if c < 1000:
		return 	c + accuFn(c+1)
	else:
		return c

print accu
print accuFn(0)