word = input("Enter a word: ")
if word.isalpha():
    uppercase_count = 0
    lowercase_count = 0

    for letter in word:
        if letter.isupper():
            uppercase_count += 1
        elif letter.islower():
            lowercase_count += 1

    print(f"Your word has {len(word)} letters.")
    print(f"Of which, {uppercase_count} are uppercase and {lowercase_count} are lowercase.")
else:
    print("[Error]: That is not a word.")
