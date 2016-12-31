# uppercase alphabet caesar cipher

ciphertext = "<YOUR_ENCRYPTED_STRING_HERE>"

for shift in range(26):
	possible_plaintext = ""
	for character in ciphertext:
		if character .isalpha():
			possible_plaintext += chr((((ord(character)-65)+shift)%26)+65)
		else:
			possible_plaintext += character

	print(possible_plaintext)