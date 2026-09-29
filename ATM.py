# ATM Simulation System


balance = 100000.00


def check_balance():
    print(f"\nCurrent Balance: ₹{balance:.2f}")


def deposit():
    global balance

    amount = float(input("Enter deposit amount: ₹"))

    if amount <= 0:
        print("Please enter a valid amount.")
    else:
        balance += amount
        print(f"₹{amount:.2f} deposited successfully!")
        print(f"Updated Balance: ₹{balance:.2f}")


def withdraw():
    global balance

    amount = float(input("Enter withdrawal amount: ₹"))

    if amount <= 0:
        print("Please enter a valid amount.")
    elif amount > balance:
        print("Insufficient balance.")
    else:
        balance -= amount
        print(f"₹{amount:.2f} withdrawn successfully!")
        print(f"Remaining Balance: ₹{balance:.2f}")


def main():
    while True:
        print("\n===== ATM SIMULATION =====")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            check_balance()

        elif choice == "2":
            deposit()

        elif choice == "3":
            withdraw()

        elif choice == "4":
            print("Thank you for using the ATM!")
            break

        else:
            print("Invalid choice. Please try again.")


main()