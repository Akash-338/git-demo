"""Demo entry point for the Git, GitHub & GitHub Actions workshop."""

from datetime import date

import pyfiglet
from colorama import Fore, init

from src.utils import calculate_age, format_date, greet, add, subtract #, multiply  # Uncomment if multiply is implemented

init(autoreset=True)


def main() -> None:
    """Print the banner and demo the utility functions."""
    print(Fore.BLUE + pyfiglet.figlet_format("Git, GitHub & Actions"))

    print(Fore.GREEN + "\n Welcome to the Git, GitHub & GitHub Actions!")
    print(Fore.YELLOW + "This is a demo application for learning version control.\n")

    print(Fore.CYAN + "Demo Functions:")
    print("-", greet("Students"))
    print("-", calculate_age(2000))
    print("-", format_date(date.today()))
    print("- Adding 5 and 3 gives", add(5, 3))
    print("- Subtracting 4 from 10 gives", subtract(10, 4))
    #print("- Multiplying 6 and 7 gives", multiply(6, 7))  # Uncomment if multiply is implemented

    print(Fore.MAGENTA + "\n Ready to start learning Git and GitHub Actions!")


if __name__ == "__main__":
    main()
