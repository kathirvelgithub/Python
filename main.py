import random

MAX_LINE = 3
MAX_BET = 100
MIN_BET = 1

ROW = 3
COL = 3

symbol_count = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}

symbol_value = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

def check_win(columns ,lines ,bet ,values):
    winning =0
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_check = column[line]
            if symbol != symbol_check:
                break
        else:
            winning +=  values[symbol] * bet
            
    return winning
            



def get_spin(rows, cols, symbols):
    all_symbols = []
    for sym, count in symbols.items():
        for _ in range(count):
            all_symbols.append(sym)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)  # **Fix: Append the value to column**
        columns.append(column)

    return columns

def print_slot(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row])

def deposit():
    while True:
        amount = input("Enter the deposit amount: $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:  # **Fix: Proper check for positive amount**
                return amount
            else:
                print("Enter a number above 0.")
        else:
            print("Enter a valid number.")

def get_lines():
    while True:
        line = input(f"Enter the number of lines to bet on (1-{MAX_LINE}): ")
        if line.isdigit():
            line = int(line)
            if 1 <= line <= MAX_LINE:  # **Fix: Ensure it's at least 1**
                return line
            else:
                print(f"Enter a number between 1 and {MAX_LINE}.")
        else:
            print("Enter a valid number.")

def get_bet():
    while True:
        amount = input(f"Enter the bet amount per line (${MIN_BET}-${MAX_BET}): ")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                return amount
            else:
                print(f"Enter a number between ${MIN_BET} and ${MAX_BET}.")
        else:
            print("Enter a valid number.")

def main_fn():
    balance = deposit()
    lines = get_lines()

    while True:
        bet = get_bet()
        total_bet = bet * lines

        if balance < total_bet:
            print(f"You do not have enough balance. Your balance is ${balance}.")
        else:
            break

    print(f"You are betting ${bet} per line on {lines} lines. Total bet: ${total_bet}")

    slot = get_spin(ROW, COL, symbol_count)
    print_slot(slot)
    win = check_win(slot,lines, bet ,symbol_value)
    print(f" you win ${win}")
    
    
main_fn()
