ORIGINAL_FILE_PATH = "../data/test_result.txt"
UPDATED_FILE_PATH = "../data/test_result_updated.txt"

with open(ORIGINAL_FILE_PATH, mode="r") as file_in:
    text_content = [line.replace("\n", "").strip() for line in file_in.readlines()]


# alphabetical sorting
text_content.sort()
with open(UPDATED_FILE_PATH, "w") as file_out:
    file_out.write("---- People sorted in alphabetical order ----\n")
    for line in text_content:
        file_out.write(f"{line}\n")
    file_out.write("\n")

text_content_dict: dict[str, int] = dict()
for line in text_content:
    name, grade = line.rsplit(" ", maxsplit=1)
    text_content_dict[name] = int(grade)

# sort people by grade
grades = {
    "F": [],
    "E": [],
    "D": [],
    "C": [],
    "B": [],
    "A": []
}

for name, grade in sorted(text_content_dict.items(), key=lambda item: item[1]):
    if grade < 20:
        grades["F"].append(f"{name} {grade}")
    elif 20 <= grade <= 29:
        grades["E"].append(f"{name} {grade}")
    elif 30 <= grade <= 39:
        grades["D"].append(f"{name} {grade}")
    elif 40 <= grade <= 49:
        grades["C"].append(f"{name} {grade}")
    elif 50 <= grade <= 59:
        grades["B"].append(f"{name} {grade}")
    elif 60 <= grade <= 70:
        grades["A"].append(f"{name} {grade}")

with open(UPDATED_FILE_PATH, "a") as file_out:
    file_out.write("---- People sorted by grades ----\n")

    for grade in grades:
        file_out.write(f"Grade {grade}:\n")
        for person in grades[grade]:
            file_out.write(f"\t- {person}\n")
