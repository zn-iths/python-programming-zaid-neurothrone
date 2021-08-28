with open("../data/pokemon_list.txt", "r") as file_in:
    in_data = [line.replace("\n", "").replace("\ufeff", "") for line in file_in.readlines()]

pokedex: dict[str, dict[str, int]] = dict()
for line in in_data:
    index, pokemon, type_ = line.split(" ", maxsplit=2)
    pokedex[pokemon] = {type_: index}

print(pokedex["Gengar"])
print(pokedex["Pikachu"])
