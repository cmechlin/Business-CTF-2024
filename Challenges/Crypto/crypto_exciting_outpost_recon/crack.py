from hashlib import sha256

LENGTH = 32


def xor_bytes(a, b):
    return bytes(x ^ y for x, y in zip(a, b))


# Known plaintext
known_plaintext = b"Great and Noble Leader of the Tariaki"

# Read the first 32 bytes of the encrypted data
with open(
    "D:\\Users\\curtismechling\\Documents\\CTFs\\Hack The Box\\Business CTF 2024\\Crypto\\crypto_exciting_outpost_recon\\output.txt",
    "r",
    encoding="utf-8",
) as f:
    encrypted_hex = f.read()

encrypted_data = bytes.fromhex(encrypted_hex)
first_chunk_encrypted = encrypted_data[:LENGTH]

# XOR the known plaintext with the encrypted data to recover the key
initial_key = xor_bytes(known_plaintext[:LENGTH], first_chunk_encrypted)

print(f"Recovered Initial Key: {initial_key.hex()}")


# Now we can decrypt the rest of the data using the recovered key
def decrypt_data(data, k):
    decrypted = b""

    for i in range(0, len(data), LENGTH):
        chunk = data[i : i + LENGTH]

        for a, b in zip(chunk, k):
            decrypted += bytes([a ^ b])

        k = sha256(k).digest()

    return decrypted.rstrip(b"\x00")  # Remove padding


decrypted_data = decrypt_data(encrypted_data, initial_key)

with open("cracked_decrypted_plaintext.txt", "wb") as f:
    f.write(decrypted_data)
