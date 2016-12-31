# lowercase alphabet caesar cipher

ciphertext = "<your_encrypted_string_here>"

for shift in range(26):
	possible_plaintext = ""
	for character in ciphertext:
		if character .isalpha():
			possible_plaintext += chr((((ord(character )-97)+shift)%26)+97)
		else:
			possible_plaintext += character

	print(possible_plaintext)