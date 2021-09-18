from plotter import draw_test_scatter_plot
from plotter import draw_user_scatter_plot
from processer import load_in_data
from processer import process_data
from shared.input import get_float_input
from shared.mathematics.distance import euclidean_distance


headers: tuple[str] = tuple()
cleaned_pichu_data = []
cleaned_pikachu_data = []
cleaned_test_data = []


def setup_baseline() -> None:
    global headers
    global cleaned_pichu_data
    global cleaned_pikachu_data
    global cleaned_test_data

    pichu_data = load_in_data("data/pichu.txt")
    headers = pichu_data.pop(0).replace("\n", "")
    headers = tuple(headers.removeprefix("(").removesuffix(")").split(", "))
    cleaned_pichu_data = process_data(pichu_data)

    pikachu_data = load_in_data("data/pikachu.txt")
    pikachu_data.pop(0).replace("\n", "")
    cleaned_pikachu_data = process_data(pikachu_data)

    test_data = load_in_data("data/test_points.txt")
    cleaned_test_data = process_data(test_data)


def get_distances(reference_point: tuple[float, float],
                  points_list: list[tuple[float, float]]) -> list[float]:
    distances = []
    for point in points_list:
        distance = euclidean_distance(point_a=reference_point, point_b=point)
        distances.append(distance)
    return distances


def get_baseline_data() -> list[dict]:
    return [
        {
            "color": "red",
            "label": "Pichu",
            "points": cleaned_pichu_data
        },
        {
            "color": "blue",
            "label": "Pikachu",
            "points": cleaned_pikachu_data
        }
    ]


def run_test_program() -> None:
    if is_plotting():
        data = get_baseline_data()
        data.append({
                "color": "green",
                "label": "Test",
                "points": cleaned_test_data
            })
        draw_test_scatter_plot(title="Pichu vs Pikachu Data Points", labels=headers, plot_data=data)

    classify(cleaned_test_data)


def run_input_program() -> None:
    x_coord = get_float_input("Enter x coordinate: ", min_=0)
    y_coord = get_float_input("Enter y coordinate: ", min_=0)
    user_point = x_coord, y_coord

    if is_plotting():
        data = get_baseline_data()
        user_data = {
                "color": "purple",
                "label": "User",
                "point": user_point
            }
        draw_user_scatter_plot(title="Pichu vs Pikachu Data Points", labels=headers,
                               plot_data=data, user_data=user_data)

    classify([user_point])


def is_plotting() -> bool:
    user_input = input("Also plot graph? (y/n): ").lower()
    return True if user_input == "y" else False


def classify(data: list[tuple[float, float]]) -> None:
    for point in data:
        pichu_distances = get_distances(point, cleaned_pichu_data)
        pikachu_distances = get_distances(point, cleaned_pikachu_data)

        pichu_min = min(pichu_distances)
        pikachu_min = min(pikachu_distances)

        print(f"Sample with (width, height): {point} classified as ", end="")
        print("Pichu" if pichu_min < pikachu_min else "Pikachu")
