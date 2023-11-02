
import random

# Number of rows and columns in the slot machine grid
ROWS = 3
COLS = 3


# Dictionary representing symbols and their counts
symbol_count = {
                'A': 2,
                'B': 4,
                'C': 6,
                'D': 8
                }

def get_slot_machine(cols, rows, symbols):
    # Creates a list of symbols based on their counts
    all_symbols = [symbol for symbol, count in symbols.items() for _ in range(count)]
    # Arranges symbols in columns and rows randomly
    columns = [[random.choice(all_symbols) for _ in range(rows)] for _ in range(cols)]
    return columns


def print_slot_machine(columns):
    # Prints the slot machine grid
    for row in range(len(columns[0])):
        for column in columns:
            print(column[row], end=" | ")
        print()

def main():
    # Generates the slot machine
    slots = get_slot_machine(ROWS, COLS, symbol_count)
    # Prints the slot machine
    print_slot_machine(slots)


# Calls the main function to run the code
main()
