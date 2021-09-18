def load_in_data(path: str) -> list[str]:
    with open(path, "r") as file_in:
        return file_in.readlines()


def process_data(in_data: list[str]) -> list[tuple[float, float]]:
    data_out: list[tuple[float, float]] = []

    for line in in_data:
        line = line.replace("\n", "")
        processed_data = clean_data(line)
        data_out += processed_data

    return data_out


def clean_data(data_in: str) -> list[tuple[float, float]]:
    data_in = data_in.replace("(", "").split("),")
    data_in = [data_.replace(" ", "").replace(")", "") for data_ in data_in]

    cleaned_data = []
    for data_ in data_in:
        str_values = data_.split(",")
        values: tuple[float, float] = (float(str_values[0]), float(str_values[1]))
        cleaned_data.append(values)
    return cleaned_data
