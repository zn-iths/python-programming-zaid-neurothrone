from string import ascii_lowercase

SWEDISH_ALPHABET = ascii_lowercase + "åäö"


def encrypt(string: str) -> str:
    encrypted = []
    for letter in string.lower():
        if letter.isalpha():
            index = SWEDISH_ALPHABET.index(letter)
            if index >= len(ascii_lowercase) - 1:
                encrypted.append(SWEDISH_ALPHABET[0])
            else:
                encrypted.append(SWEDISH_ALPHABET[index + 1])
        else:
            encrypted.append(letter)
    return "".join(encrypted)


def decrypt(string: str) -> str:
    decrypted = []
    for letter in string.lower():
        if letter.isalpha():
            index = SWEDISH_ALPHABET.index(letter)
            if index <= 0:
                decrypted.append(SWEDISH_ALPHABET[-1])
            else:
                decrypted.append(SWEDISH_ALPHABET[index - 1])
        else:
            decrypted.append(letter)
    return "".join(decrypted)


actions = ["e", "d"]
print("---- This script can encrypt or decrypt your message ----")

while True:
    message = input("Enter your message: ")
    action = input("Enter e to encrypt or d to decrypt your message: ")
    if action not in actions:
        print("[Error]: That is not a valid command.")
    else:
        if action == "e":
            result = encrypt(message)
            print(f"Encrypted message: {result}")
        else:
            result = decrypt(message)
            print(f"Decrypted message: {result}")

    if input("Run again? (y/n): ") == "n":
        break
    print()
