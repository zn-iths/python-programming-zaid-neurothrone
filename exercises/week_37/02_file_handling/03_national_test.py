import matplotlib.patches as mp
import matplotlib.pyplot as plt


def get_clean_data(file_path: str) -> dict[str, float]:
    with open(file_path, mode="r") as file_in:
        in_data = file_in.readlines()
    out_data: dict[str, float] = dict()

    for index, _ in enumerate(in_data):
        in_data[index] = in_data[index].replace("\n", "").replace("%", "")
        grade, score = in_data[index].split(" ", maxsplit=1)
        out_data[grade] = float(score)

    return out_data


COLORS = "green", "blue", "teal", "yellow", "orange", "red"
EXPLODE = 0, 0, 0, 0, 0, 0.1
LABELS = "A", "B", "C", "D", "E", "F"


def plot_pie_chart(plot, title, values) -> None:
    colors, explodes, labels, values = zip(
        *((color, explode, label, value) for
          color, explode, label, value in
          zip(COLORS, EXPLODE, LABELS, values)
          if value > 0))
    plot.pie(values,
             autopct="%1.1f%%",
             colors=colors,
             labels=labels,
             explode=explodes)
    plot.set_title(title)


data_a = get_clean_data(file_path="../data/NPvt19Ma2A.txt")
data_b = get_clean_data(file_path="../data/NPvt19Ma2C.txt")

figure, (ax1, ax2) = plt.subplots(1, 2)

plot_pie_chart(ax1, "Ma2A", data_a.values())
plot_pie_chart(ax2, "Ma2C", data_b.values())

patches = []
for color_, label_ in zip(COLORS, LABELS):
    patches.append(mp.Patch(color=color_, label=label_))

figure.legend(title="Grades:", handles=patches)
figure.suptitle("National tests results in Ma2A & Ma2C")

plt.show()
