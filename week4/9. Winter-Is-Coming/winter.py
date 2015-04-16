# winter.py

def winter_is_coming(seasons):

	index = 0
	end = len(seasons)
	counter = 0

	while index < end:	
		if seasons[index] == 'winter':
			counter = 0
		else:
			counter += 1
		if counter >= 5:
			return True


		index += 1

	return False

print(winter_is_coming(["spring", "winter", "winter","spring", "winter", "winter", "winter"]))
print(winter_is_coming(["spring", "winter", "spring", "spring", "spring", "spring", "spring"]))
