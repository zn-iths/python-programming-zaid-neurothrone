def is_palindrome(string: str) -> bool:
    return string.lower() == string[::-1].lower()


print("---- This script will check if your sequence is a palindrome ----")
sequence = input("Enter a sequence of characters: ")
print("Is a palindrome." if is_palindrome(sequence) else "NOT a palindrome.")
