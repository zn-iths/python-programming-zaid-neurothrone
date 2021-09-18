from core import run_input_program
from core import run_test_program

HELP = """
Option 1: will classify the test data against the baseline.
Option 2: will classify the point entered by the user to the baseline.
Option 3: will print this.
Option 0: will quit the program.
"""


def print_help() -> None:
    print(HELP)


def print_menu() -> None:
    print("\n---- Menu ----")
    print("1. Run test classifier program")
    print("2. Run user classifier program")
    print("3. Help")
    print("0. Quit")
    print("--------------\n")


def menu(selection: int) -> None:
    if selection == 1:
        run_test_program()
    elif selection == 2:
        run_input_program()
    elif selection == 3:
        print_help()
