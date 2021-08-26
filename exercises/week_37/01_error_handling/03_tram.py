def int_input(message: str) -> int:
    while True:
        try:
            user_input = int(input(message))
            if user_input > 0:
                return user_input
            else:
                print("[Error]: Please enter a number higher than zero.")
        except ValueError:
            print("[Error]: Only enter integers.")


print("---- Hello, I am Tram Bot ----")
trams_per_month = int_input(
    message="How many times do you want to take the tram in one month? ")
cost_per_ticket = int_input(
    message="What is the price for one ticket? ")
cost_monthly_card = int_input(
    message="What is the cost for a monthly card? ")

cost_tickets_month = trams_per_month * cost_per_ticket
print(f"\nTaking {trams_per_month} trams per month will cost you "
      f"{cost_tickets_month} if you buy tickets and {cost_monthly_card} with card.")
if cost_monthly_card < cost_tickets_month:
    print("It is cheaper to buy a monthly card.")
elif cost_monthly_card == cost_tickets_month:
    print("The price is equal, go with what you prefer.")
else:
    print("It is cheaper to buy tickets than the monthly card.")

# Test Case: VastTrafik
# Travels per month: 24
# Cost per ticket:   34 kr
# Cost monthly card: 795 kr

# Test Case: VastTrafik (Student)
# Travels per month: 24
# Cost per ticket:   26 kr
# Cost monthly card: 595 kr
