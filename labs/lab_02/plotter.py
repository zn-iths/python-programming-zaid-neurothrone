from matplotlib import pyplot as plt


def draw_baseline(plt_, plot_data: list[dict]) -> None:
    for data_dict in plot_data:
        x_points, y_points = zip(*data_dict["points"])
        plt_.scatter(x_points, y_points, color=data_dict["color"], label=data_dict["label"])


def draw_test_scatter_plot(title: str,
                           labels: tuple[str],
                           plot_data: list[dict]) -> None:
    plt.title(title)
    plt.xlabel(labels[0])
    plt.ylabel(labels[1])

    draw_baseline(plt, plot_data)

    plt.legend(loc="lower right")
    plt.show()


def draw_user_scatter_plot(title: str,
                           labels: tuple[str],
                           plot_data: list[dict],
                           user_data: dict) -> None:
    plt.title(title)
    plt.xlabel(labels[0])
    plt.ylabel(labels[1])

    draw_baseline(plt, plot_data)

    x_point, y_point = user_data["point"]
    plt.scatter(x_point, y_point, color=user_data["color"], label=user_data["label"])

    plt.legend(loc="lower right")
    plt.show()
