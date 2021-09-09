from matplotlib import pyplot as plt

from shared.mathematics.distance import euclidean_distance
from shared.input.integer import get_int_input


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


def get_distances(reference_point: tuple[float, float],
                  points_list: list[tuple[float, float]]) -> list[float]:
    distances = []
    for point in points_list:
        distance = euclidean_distance(point_a=reference_point, point_b=point)
        distances.append(distance)
    return distances


def scatter_plot(title: str, labels: tuple[str], plot_data: list[dict]) -> None:
    plt.title(title)
    plt.xlabel(labels[0])
    plt.ylabel(labels[1])

    for data_dict in plot_data:
        x_points, y_points = zip(*data_dict["points"])
        plt.scatter(x_points, y_points, color=data_dict["color"], label=data_dict["label"])

    plt.legend(loc="lower right")
    plt.show()


def run_test_program():
    user_input = input("Also plot graph? (y/n): ").lower()
    is_plotting = True if user_input == "y" else False

    pichu_data = load_in_data("data/pichu.txt")
    pichu_labels = pichu_data.pop(0).replace("\n", "")
    cleaned_pichu_data = process_data(pichu_data)

    pikachu_data = load_in_data("data/pikachu.txt")
    pikachu_labels = pikachu_data.pop(0).replace("\n", "")
    cleaned_pikachu_data = process_data(pikachu_data)

    test_data = load_in_data("data/test_points.txt")
    cleaned_test_data = process_data(test_data)

    if is_plotting:
        data = [
            {
                "color": "red",
                "label": "Pichu",
                "points": cleaned_pichu_data
            },
            {
                "color": "blue",
                "label": "Pikachu",
                "points": cleaned_pikachu_data
            },
            {
                "color": "green",
                "label": "Test",
                "points": cleaned_test_data
            }
        ]
        plot_labels = tuple(pichu_labels.removeprefix("(").removesuffix(")").split(", "))
        scatter_plot(title="Pichu vs Pikachu Data Points", labels=plot_labels, plot_data=data)

    for test_point in cleaned_test_data:
        pichu_distances = get_distances(test_point, cleaned_pichu_data)
        pikachu_distances = get_distances(test_point, cleaned_pikachu_data)

        pichu_min = min(pichu_distances)
        pikachu_min = min(pikachu_distances)

        print(f"Sample with (width, height): {test_point} classified as ", end="")
        print("Pichu" if pichu_min < pikachu_min else "Pikachu")


def run_input_program():
    print("Input program called")


def print_help() -> None:
    print("Help called")


def print_menu() -> None:
    print("\n---- Menu ----")
    print("1. Run test program")
    print("2. Run input program")
    print("3. Help")
    print("0. Quit")
    print("--------------\n")


def menu(selection: int) -> None:
    if selection == 1:
        run_test_program()
    elif selection == 2:
        run_input_program()
    elif selection == 3:
        print_help()


def run():
    print("Starting Pichu vs Pikachu Classifier...")

    is_running = True
    while is_running:
        print_menu()
        selection = get_int_input("Enter selection: ", min_=0, max_=3)
        if (is_running := selection) != 0:
            menu(selection)
    print("Terminating program...")


def main():
    run()


if __name__ == "__main__":
    main()
