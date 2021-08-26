foods = ["vegetarisk lasagne", "spaghetti", "fisk", "grönsakssoppa", "pannkakor"]
weekdays = ["monday", "tuesday", "wednesday", "thursday", "friday"]

for food, weekday in zip(foods, weekdays):
    print(f"Today on {weekday} we serve {food}")
