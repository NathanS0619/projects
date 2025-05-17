orig_balance = 1500
while True:
    try:
        trans = int(input("Hello! How much would you like to withdraw? $"))
        if trans <= 0:
            print("Please enter a positive value")
            continue
        elif trans > 1500:
            print("Insufficient funds!")
            continue

        new_balance = orig_balance - trans
    except ValueError:
        print("Please enter a dollar amount")
        continue
    else:
        print("Your new account balance is: $", new_balance)
        break
    finally:
        print("Remaining balance: $", new_balance)