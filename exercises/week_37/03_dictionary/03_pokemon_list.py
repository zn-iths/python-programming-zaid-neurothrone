with open("../data/pokemon_list.txt", "r") as file_in:
    in_data = file_in.readlines()


for index, _ in enumerate(in_data):
    in_data[index] = in_data[index].replace("\n", "").replace("\ufeff", "")

pokedex: dict[str, dict[str, int]] = dict()
for line in in_data:
    index, pokemon, type_ = line.split(" ", maxsplit=2)
    pokedex[pokemon] = {type_: index}

print(pokedex["Gengar"])
print(pokedex["Pikachu"])
