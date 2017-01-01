# lowercase alphabet rot13

ciphertext = "<YOUR_ENCRYPTED_STRING_HERE>"

plaintext = ""
for character in ciphertext:
	if character .isalpha():
		plaintext += chr((((ord(character )-65)+13)%26)+65)
	else:
		plaintext += character

print(plaintext)