import hashlib
import itertools
import string


def md5_cracker(hash_to_crack, max_length):
    # Create an iterable that will go through all combinations of letters
    characters = (
        string.ascii_lowercase
        + string.digits
        + string.punctuation
        + string.ascii_uppercase
    )
    for length in range(6, max_length + 1):
        for guess in itertools.product(characters, repeat=length):
            guess = "".join(guess)
            hashed_guess = hashlib.md5(guess.encode("utf-8")).hexdigest()
            if hashed_guess == hash_to_crack:
                return guess
    return None


if __name__ == "__main__":
    hash_to_crack = "d87559a87bea8bebe93b5c067909dbebfa371e535597c50cbd0e92b26d2d58a733e0d92b950621dc37a7523611888da6ce0266518cdd5c08b13e050e5487d678feaa30e2910275a1e70912c011b6e408ce448ccc070946089413e9750b7a9685534742f3e43066154a7d06c343b9fc2560da668b9d1dff2cdf9d9fe6791c09c65e3a3064fa128315f3f76cf185d905bdad08acf48a14bfd2ddd5bb8c63f7785b7195ac28f607e2bad049aee6d257cfc0d2f19094c3a9c484145a1949e5fdfb64618b0a61f9b754b50855ab69ba2f48db614eeafebdacab14b4f50e883ef9e78db8be8240461c861e543606358be0ce24982237baaf0d99cc5580"
    # hash_to_crack = input("Enter the MD5 hash: ").strip()
    max_length = 8
    # max_length = int(input("Enter the maximum length of the password: ").strip())
    result = md5_cracker(hash_to_crack, max_length)

    if result:
        print(f"Hash cracked! The password is: {result}")
    else:
        print("Failed to crack the hash.")
