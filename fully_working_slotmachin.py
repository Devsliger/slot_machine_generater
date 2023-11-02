# Import the random module for generating random values
import random

# Constants for the game rules
MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1
ROWS = 3
COLS = 3

# Dictionary defining the count of each symbol in the slot machine
symbol_count = {
    'A': 2,
    'B': 4,
    'C': 6,
    'D': 8
}

# Dictionary defining the values associated with each symbol
symbol_value = {
    'A': 5,
    'B': 4,
    'C': 3,
    'D': 2
}

# Function to check if the player has won and calculate the winnings
def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)
    return winnings, winning_lines

# Function to generate the slot machine grid
def get_slot_machine(cols, rows, symbols):
    # Create a list containing all symbols based on their counts
    all_symbols = []
    for symbol, count in symbols.items():
        for _ in range(count):
            all_symbols.append(symbol)

    # Create columns with random symbols based on rows and columns
    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)
    return columns

# Function to print the slot machine grid
def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for column in columns:
            print(column[row], end=" | ")
        print()

# Function to take user deposit input
def deposit():
    while True:
        amount = input("What would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0")
        else:
            print("Enter a valid amount $")
    return amount

# Function to take user input for the number of lines to bet on
def get_num_of_lines():
    while True:
        lines = input("Enter number of lines to bet on (1 - " + str(MAX_LINES) + "): ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines")
        else:
            print("Enter a valid amount")
    return lines

# Function to take user input for the bet amount
def get_bet():
    while True:
        amount = input("What would you like to bet on each line? $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}")
        else:
            print("Enter a valid amount $")
    return amount

# Main function to execute the game logic
def main():
    # Get initial deposit from the user
    balance = deposit()

    # Get the number of lines to bet on
    lines = get_num_of_lines()

    # Get the bet amount from the user
    while True:
        bet = get_bet()
        total_bet = bet * lines

        # Check if the total bet exceeds the available balance
        if total_bet > balance:
            print("You do not have enough balance.")
        else:
            break

    # Print the bet information
    print(f"You are betting ${bet} on {lines} lines. Your total bet is ${total_bet}")

    # Generate the slot machine grid
    slots = get_slot_machine(ROWS, COLS, symbol_count)

    # Print the slot machine grid
    print_slot_machine(slots)

    # Check for winnings and print the results
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f'Your winnings are ${winnings}')
    print(f'You won on lines:', *winning_lines)

# Call the main function to run the game
main()
