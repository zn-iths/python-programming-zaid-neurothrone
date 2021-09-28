from core import setup_baseline
from menu import menu
from menu import print_menu

from shared.input import get_int_input


def main() -> None:
    setup_baseline()
    print("Starting Pichu vs Pikachu Classifier...")

    is_running = True
    while is_running:
        print_menu()
        selection = get_int_input("Enter selection: ", min_=0, max_=3)
        if (is_running := selection) != 0:
            menu(selection)
    print("Terminating program...")


if __name__ == "__main__":
    main()
