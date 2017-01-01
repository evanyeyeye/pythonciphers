# polybius square cipher with a default encryption grid

import string

alphabet = string.ascii_lowercase.replace('j', '') # might have to fix some plaintext 'i's to be 'j's

ciphertext = "<your_encrypted_string_here>"

mapping = {
	'A': '1',
	'B': '2',
	'C': '3',
	'D': '4',
	'E': '5'
}

fixed_ciphertext = ""
for character in ciphertext:
	if character.isalpha():
		fixed_ciphertext += mapping[character.upper()]
	else:
		fixed_ciphertext += character

grid = []
for row in range(5):
	grid.append(alphabet[:5])
	alphabet = alphabet[5:]

plaintext = ""
for index in range(0, len(fixed_ciphertext), 2):
	plaintext += grid[int(fixed_ciphertext[index])-1][int(fixed_ciphertext[index+1])-1]

print (plaintext)