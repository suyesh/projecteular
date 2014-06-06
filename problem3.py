
#problem3 url http://projecteuler.net/problem=3

def prime_factor(num):
	i = 2
	while i * i < num:
		while num % i == 0:
			num = num / i
		i = i +1
	return num 

print prime_factor(600851475143)