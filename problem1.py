#problem1 url http://projecteuler.net/problem=1

def divisible_by(num1, num2):
	numbers = []
	for num in xrange(1,1000):
		if num % num1 == 0 or num % num2 == 0:
			numbers.append(num)
		
	return sum(numbers)

print divisible_by(3,5)

