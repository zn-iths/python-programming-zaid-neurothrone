curriculum: dict[str, int] = {
    "Intro to AI": 5,
    "Python programming": 40,
    "Data processing": 25,
    "Visualization, presentation & storytelling": 20,
    "Statistical methods": 30,
    "Machine learning": 45,
    "Deep machine learning": 40,
    "Databases": 25,
    "LIA 1": 40,
    "Practical machine learning": 35,
    "Project methodology": 10,
    "LIA 2": 70,
    "Master thesis": 15
}

print(f"---- Curriculum for AI & ML Engineer at ITHS ----\n")
for course, credit in curriculum.items():
    print(f"{course} - {credit}p")
print(f"\nTotal credits: {sum(curriculum.values())}")
