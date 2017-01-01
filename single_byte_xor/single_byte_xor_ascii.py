# single byte xor for ASCII string

ciphertext = "<your_encrypted_string_here>"

for byte in range(256):
	possible_plaintext = ""
	for character in ciphertext:
		possible_plaintext += chr(ord(character)^byte)

	print(possible_plaintext)