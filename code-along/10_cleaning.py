import re

FILE_IN_PATH = "./data/quotes_uncleaned.txt"
FILE_OUT_PATH = "./data/quotes_cleaned.txt"

with open(FILE_IN_PATH, "r") as file_in:
    uncleaned_data = [line.replace("\n", "") for line in file_in.readlines()]
    uncleaned_data = [re.sub(" +", " ", line) for line in uncleaned_data if line]

cleaned_data = []
for line in uncleaned_data:
    quote, author = line.split("-", maxsplit=1)
    cleaned_quote = " ".join([word for word in quote.strip().split(" ") if word])
    cleaned_author = author.strip()
    cleaned_data.append((cleaned_author, cleaned_quote))

output = "Famous quotes\n\n"
for index, (author, quote) in enumerate(cleaned_data):
    output += f"{index + 1}. {quote} - {author}\n"
authors = ", ".join(sorted({author for (author, quote) in cleaned_data}))
output += f"\nAuthors: {authors}"

with open(FILE_OUT_PATH, "w") as file_out:
    file_out.write(output)
