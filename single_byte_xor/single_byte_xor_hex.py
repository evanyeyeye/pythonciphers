# single byte xor for hex string

ciphertext = "<your_encrypted_string_here>"
ciphertext = "130e5a0d1b095a1b5a1e1b08115a1b141e5a090e150817035a14131d120e"

for byte in range(256):
	possible_plaintext = ""
	for index in range(0, len(ciphertext), 2):
		possible_plaintext += chr(int(ciphertext[index:index+2], 16)^byte)

	print(possible_plaintext)