# pairs.py

def count_zero_neighbours(numbers):
	
	i = 0
	end = len(numbers)

	counter = 0

	while i < end:
		if i + 1 < end:
			if numbers[i] + numbers[i + 1] == 0:
				counter += 1

		i += 1

	return counter


print(count_zero_neighbours([1, 2, -2, 0, 0, 5, -5]))
