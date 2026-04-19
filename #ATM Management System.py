#ATM Management System (Python)
pin = 121490
balance = 10000

entered_pin = int(input("Enter your PIN: "))

if entered_pin != pin:
    print("Mission Failed ❌")
else:
    while True:
        print("\nATM MENU")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            print("Balance:", balance)

        elif choice == 2:
            amount = float(input("Enter amount to deposit: "))
            balance += amount
            print("Amount Deposited")

        elif choice == 3:
            amount = float(input("Enter amount to withdraw: "))
            if amount > balance:
                print("Insufficient Balance")
            else:
                balance -= amount
                print("Please collect cash")

        elif choice == 4:
            print("Thank you & please collect u r card!")
            break

        else:
            print("Invalid choice")