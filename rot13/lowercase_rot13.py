# lowercase alphabet rot13

ciphertext = "<your_encrypted_string_here>"

plaintext = ""
for character in ciphertext:
	if character .isalpha():
		plaintext += chr((((ord(character )-97)+13)%26)+97)
	else:
		plaintext += character

print(plaintext)