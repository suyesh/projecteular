#problem2 url http://projecteuler.net/problem=2

def fib(n):
	if n == 1:
		return 1
	elif n == 0:
		return 0
	else:
		return fib(n-1) + fib(n-2)

num = 0
num2 = 0
while fib(num2) <= 4000000:
	if fib(num2) % 2 == 0:
		num = num + fib(num2)
	num2 += 1

print num
