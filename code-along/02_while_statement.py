# 1 litre milk contains 1 500 000 bacteria in rooms temperature
# The amount of bacteria increase by 50% per hour in room temperature
# Milk will sour when the amount of bacteria is 10 000 000 or greater
# How many hours does it take for the milk to sour (whole hours)

RATE = 1.5
START_AMOUNT = 1_500_000
THRESHOLD = 10_000_000

hours = 0
current_value = START_AMOUNT
print(f"Initial amount of bacteria: {current_value:,}")
while current_value < THRESHOLD:
    hours += 1
    current_value *= RATE
    print(f"hour: {hours}, bacteria amount: {current_value:,.0f}")

print(f"It takes {hours} hours for 1 litre milk to sour in room temperature.")
