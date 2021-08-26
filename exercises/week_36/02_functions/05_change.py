swedish_bank_notes_coins: dict[str, int] = {
    "1000-lapp": 1000,
    "200-lapp": 200,
    "50-lapp": 50,
    "20-lapp": 20,
    "10-krona": 10,
    "5-krona": 5,
    "2-krona": 2
}


def compute_change(money: int) -> None:
    remaining_money = money
    for name, value in swedish_bank_notes_coins.items():
        remainder = int(remaining_money % value)
        exchanged = remaining_money - remainder
        remaining_money -= exchanged
        print(f"{exchanged // value}st {name}")


print("--- This script computes the change of bank notes and coins you get from an amount ---")
money_to_exchange = int(input("Enter an amount of money to exchange: "))
compute_change(money=money_to_exchange)
