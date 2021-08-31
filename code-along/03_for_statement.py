from math import exp
from matplotlib import pyplot as plt

# formula for pasta consumption in Sweden
# P = 0.791 * e^0.0526*t
# P = yearly pasta consumption in kg per person and t is time in year after the year 1960

# a) Assume the pasta consumption continues to increase according to the model.
#    Determine which year the yearly pasta consumption reaches 15 kg per person
# -  Year 2016

# b) The model is realistic from the year 1960 to today. Evaluate how well the model
#    represents reality at the end of this century
# -  Exponential growth; the model does not represent reality on a larger time scale.


def compute_pasta_consumption(year: int) -> float:
    return 0.791 * exp(0.0526 * year)


pasta_per_year = []

START_YEAR = 1960
END_YEAR = 2100
TARGET_RANGE = range(START_YEAR, END_YEAR + 1)
TARGET_CONSUMPTION = 15
has_reached_target = False
for current_year in TARGET_RANGE:
    pasta_consumption = compute_pasta_consumption(current_year - START_YEAR)
    pasta_per_year.append(pasta_consumption)

    if not has_reached_target and pasta_consumption >= TARGET_CONSUMPTION:
        has_reached_target = True
        print(f"On the year {current_year} the pasta consumption reaches 15 kg per person.")

plt.figure(dpi=100)
plt.plot(TARGET_RANGE, pasta_per_year)
plt.xlabel("Year")
plt.ylabel("Pasta consumption in kg")
plt.title("Pasta consumption model for kg per person from year 1960")
plt.show()
