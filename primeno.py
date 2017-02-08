import math

n= input ("Please enter a number: ")

def primeno(n):


	for i in range(n):
		if n%3 == 0 or n%5 == 0 or n%2 == 0:
			return False
	return True
prime=[]
prime.append(2)
prime.append(3)
prime.append(5)
for i in range(n):
	if primeno(i):
		prime.append(i)
print(prime)
