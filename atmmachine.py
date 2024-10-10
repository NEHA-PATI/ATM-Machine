import time

print('Please Enter your ATM Card')

time.sleep(2)

password = 1234
pin = input('Enter your ATM Pin: ')

try:
    pin = int(pin)  # Convert input to integer
except ValueError:
    print('Invalid PIN format. Please enter numeric digits only.')
    exit()

balance = 5000

if pin == password:
    while True:
        print('''
            1==balance
            2==Withdraw Balance
            3==Deposit Balance
            4==Pin_Change
            5==Exit
            '''
        )
        try:
            option = int(input('Please Enter your choice: '))
        except ValueError:
            print('Please Enter Valid Option')
            continue

        if option == 1:
            print(f'Your current balance is {balance}')

        elif option == 2:
            try:
                withdraw_amount = int(input('Please enter withdrawal amount: '))
                if withdraw_amount > balance:
                    print('Insufficient balance.')
                else:
                    balance = balance - withdraw_amount
                    print(f'{withdraw_amount} is debited from your account')
                    print(f'Your updated balance is {balance}')
            except ValueError:
                print('Invalid input. Please enter a valid amount.')

        elif option == 3:
            try:
                deposit_amount = int(input('Please enter deposit amount: '))
                balance = balance + deposit_amount
                print(f'{deposit_amount} is credited to your account')
                print(f'Your updated balance is {balance}')
            except ValueError:
                print('Invalid input. Please enter a valid amount.')

        elif option == 4:
            try:
                pin = 1234
                attempts = 3
                while attempts > 0:
                    entered_pin = int(input("Enter current PIN: "))
                    if entered_pin == pin:
                        new_pin = int(input("Enter new PIN: "))
                        confirm_pin = int(input("Confirm new PIN: "))
                        if new_pin == confirm_pin:
                            pin = new_pin
                            print("PIN changed successfully.")
                            break
                        else:
                            print("New PINs do not match.")
                    else:
                        attempts -= 1
                        print("Incorrect PIN. Attempts remaining:", attempts)
                if attempts == 0:
                    print("Too many failed attempts. Account locked.")
            except ValueError:
                print('Invalid input. Please enter a valid amount.')

        elif option == 5:
            break
        else:
            print('Invalid option. Please choose from 1 to 4.')
else:
    print('Wrong PIN. Please try again.')
