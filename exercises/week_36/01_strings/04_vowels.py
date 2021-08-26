def vowel_count(string: str) -> int:
    """Returns the amount of vowels in a string."""
    vowels = {"a", "e", "i", "o", "u", "y"}
    counter = 0
    for letter in string:
        if letter in vowels:
            counter += 1
    return counter


SENTENCE = "Pure mathematics is, in its way, the poetry of logical ideas"
print(f"The sentence ['{SENTENCE}'] has {vowel_count(SENTENCE)} vowels.")
