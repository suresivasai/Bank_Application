accounts = []

def find_account(name, pin):
    for acc in accounts:
        if acc['name'] == name and acc['pin'] == pin:
            return acc
    return None

while True:
    print("\n1) New Account")
    print("2) Deposit")
    print("3) Withdraw")
    print("4) Balance Enquiry")
    print("5) Exit\n")

    choice = int(input("Enter Your Choice: "))

    if choice == 1:
        name = input("Enter A/C holder name: ")
        pin = int(input("Set 4-digit PIN: "))
        balance = int(input("Enter initial deposit: "))
        accounts.append({"name": name, "pin": pin, "balance": balance})
        print("Account created successfully!")

    elif choice in [2, 3, 4]:
        name = input("Enter A/C holder name: ")
        pin = int(input("Enter PIN: "))
        acc = find_account(name, pin)
        
        if acc:
            if choice == 2:
                amt = int(input("Enter deposit amount: "))
                acc['balance'] += amt
                print("Deposit successful. Updated Balance:", acc['balance'])
            elif choice == 3:
                amt = int(input("Enter withdrawal amount: "))
                if acc['balance'] >= amt:
                    acc['balance'] -= amt
                    print("Withdrawal successful. Remaining Balance:", acc['balance'])
                else:
                    print("Insufficient balance.")
            elif choice == 4:
                print("Current Balance:", acc['balance'])
        else:
            print("Invalid account details.")

    elif choice == 5:
        print("Thank you for using ABC Bank.")
        break

    else:
        print("Invalid Choice. Try again.")
