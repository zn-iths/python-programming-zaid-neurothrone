from matplotlib import pyplot as plt

from shared.mathematics.distance import euclidean_distance


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
    data_in = [data.replace(" ", "").replace(")", "") for data in data_in]

    cleaned_data = []
    for data in data_in:
        str_values = data.split(",")
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


if __name__ == "__main__":
    # TODO: 1. read in data and save to appropriate data structures
    pichu_data = load_in_data("data/pichu.txt")
    pichu_labels = pichu_data.pop(0).replace("\n", "")
    cleaned_pichu_data = process_data(pichu_data)

    pikachu_data = load_in_data("data/pikachu.txt")
    pikachu_labels = pikachu_data.pop(0).replace("\n", "")
    cleaned_pikachu_data = process_data(pikachu_data)

    # TODO: 2. plot all points with different colors in the same window
    plot_labels = pichu_labels.removeprefix("(").removesuffix(")").split(", ")
    plt.title("Pichu vs Pikachu Data Points")
    plt.xlabel(plot_labels[0])
    plt.ylabel(plot_labels[1])

    POINT_SCALE = 50

    # TODO: 2.a) plot pichu
    pichu_x_points, pichu_y_points = zip(*cleaned_pichu_data)
    plt.scatter(pichu_x_points, pichu_y_points, color="red", label="Pichu", s=POINT_SCALE)

    # TODO: 2.b) plot pikachu
    pikachu_x_points, pikachu_y_points = zip(*cleaned_pikachu_data)
    plt.scatter(pikachu_x_points, pikachu_y_points, color="blue", label="Pikachu", s=POINT_SCALE)

    # TODO: 3. read in test points
    test_data = load_in_data("data/test_points.txt")
    cleaned_test_data = process_data(test_data)

    test_x_points, test_y_points = zip(*cleaned_test_data)
    plt.scatter(test_x_points, test_y_points, color="green", label="Test")

    plt.legend(loc="lower right")
    plt.show()

    # TODO: 4. compare distance between each test point and other points
    #       - find min of test point vs pichu points
    #       - find min of test point vs pikachu points
    for test_point in cleaned_test_data:
        pichu_distances = get_distances(test_point, cleaned_pichu_data)
        pikachu_distances = get_distances(test_point, cleaned_pikachu_data)

        pichu_min = min(pichu_distances)
        pikachu_min = min(pikachu_distances)

        # TODO: 5. classification
        #       - does the point belong to Pichu?
        #       - YES -> classify as Pichu
        #       - NO  -> classify as Pikachu
        print(f"Sample with (width, height): {test_point} classified as ", end="")
        print("Pichu" if pichu_min < pikachu_min else "Pikachu")
