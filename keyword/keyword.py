# keyword cipher

import string

ciphertext = '<your_encrypted_string_here>'

alphabet = string.ascii_lowercase # string.ascii_uppercase 

f = open("output.txt", "w+")

def fix_word(word, index):
	if index == len(word):
		for letter in range(index):		
			if word[index-1] == word[letter]:
				word = word[:index-1]
				break
		return word
	for letter in range(index):
		if word[index] == word[letter]:
			word = word[:index] + word[index+1:]
			break
	return fix_word(word, index+1)

def create_key(word):
	key = alphabet
	for letter in word:
		key = key.replace(letter, '')
	key = word + key
	return dict(zip(list(key), list(alphabet)))

def decode(key):
	mapping = create_key(fix_word(key, 0))
	plaintext = ciphertext
	for i in range(len(plaintext)):
		try:
			plaintext = plaintext[:i] + mapping[plaintext[i]] + plaintext[i+1:]
		except KeyError:
			continue
	return plaintext + "\n"

with open("words.txt", "r") as file:
	for line in file:
		f.write(decode(line.lower()))
