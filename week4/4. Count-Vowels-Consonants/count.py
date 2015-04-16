# count.py

def count_vowels_consonants(word):

    vowls = "aeiouyAEIOUY"
    cons = "bcdfghjklmnpqrstvwxzBCDFGHJKLMNPQRSTVWXZ"

    counted = {
	    "vowels": 0,
	    "consonants": 0
    }


    for i in word:
	    if i in vowls:
	    	counted["vowels"] += 1

	    elif i in cons:
	    	counted["consonants"] += 1

    return counted


print(count_vowels_consonants("aBcDeFg"))
