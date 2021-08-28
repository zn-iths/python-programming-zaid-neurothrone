from platform import system

from colorama import Fore
from colorama import init

from shared.week_38_oop.village import Village

if (system()) == "Windows":
    init()  # makes colorama work for windows


def print_menu() -> None:
    """Prints the menu of this program."""

    print(f"{Fore.CYAN}---------------------------------")
    print("1. List current stock of Warehouse")
    print("2. List general status of Village")
    print("3. Skip 1 hour")
    print("0. Quit")
    print(f"---------------------------------{Fore.RESET}")


def get_int_input(min_: int, max_: int) -> int:
    """Get integer based user input.

    Args:
        min_ (int): The minimum acceptable int value.
        max_ (int): The maximum acceptable int value.

    Returns:
        int: the integer input from the user
    """
    while True:
        try:
            user_input = int(input("Enter your selection: "))
            if min_ <= user_input <= max_ + 1:
                return user_input
            else:
                print(f"{Fore.RED}[Error]: {Fore.RESET}Invalid selection. Try again.")
        except ValueError:
            print(f"{Fore.RED}[Error]: {Fore.RESET}Invalid input. Only enter an integer.")


def run() -> None:
    """Initializes the program and runs it's loop."""

    village = Village()
    menu_actions: dict = {
        1: village.warehouse.print_current_stock,
        2: village.print_village_status,
        3: village.skip_hour
    }

    print("---- Welcome to Travian Mini ----")

    is_running = True
    while is_running:
        print_menu()
        if (selection := get_int_input(min_=0, max_=len(menu_actions) - 1)) == 0:
            break
        menu_actions[selection]()
    print(f"{Fore.CYAN}Terminating program...")


if __name__ == "__main__":
    run()
