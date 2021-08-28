with open("../data/morse.txt", "r") as file_in:
    in_data = [line.replace("\n", "") for line in file_in.readlines()]

morse_interpreter: dict[str, str] = dict()

for line in in_data:
    letter, code = line.split(": ", maxsplit=1)
    morse_interpreter[letter.lower()] = code

print("---- Welcome to Morse Code Translator ----")
while True:
    message = input("Enter your message to have it translated to morse code:\n")
    translation = []
    try:
        for letter in message.lower():
            if letter.isalpha():
                translation.append(morse_interpreter[letter].lower())
            elif letter.isspace():
                translation.append(" ")
        print(f"Translation: {''.join(translation)}")
    except KeyError:
        print("[Error]: Only enter alphabetical letters of either the English or Swedish language.")

    if input("Run again (y/n)? ") == "n":
        break
