import account_info as account_info
from pin_maker import makePin
from iban_maker import makeIban

#=======================================================================================================
iban: str = makeIban()
pin: str = makePin()

print("\nYour account was created!")
print(f"\nOwner of card is: {account_info.owner}")
print(f"Iban of card is: {iban}")
print(f"PIN of card is: {pin}")

wrong_tries = 0

while True:
    conf = input("\nWhat operation do you want to do?(deposit/withdrawal/reference/Quit): ").lower()

    if conf == "reference":
        pin_identification = input("\nEnter your pin: ")
        if pin_identification == pin:
            print(f"\nOwner: {account_info.owner}")
            print(f"IBAN: {iban}")
            print(f"Balance: {account_info.start_balance:.2f} {account_info.type_of_currency}")
    elif conf == "deposit":
        pin_identification = input("\nEnter your pin: ")
        if pin_identification == pin:
            type_of_currency_you_want_to_deposit = input("Enter the currency you will deposit('BGN', 'USD', 'EUR'): ").lower()
            deposit = float(input("Enter the amount you will deposit: "))
            if type_of_currency_you_want_to_deposit == account_info.type_of_currency:
                account_info.start_balance += deposit
            elif account_info.type_of_currency == "usd":
                if type_of_currency_you_want_to_deposit == "bgn":
                    account_info.start_balance += deposit * 0.56
                elif type_of_currency_you_want_to_deposit == "eur":
                    account_info.start_balance += deposit * 1.09
            elif account_info.type_of_currency == "eur":
                if type_of_currency_you_want_to_deposit == "usd":
                    account_info.start_balance += deposit * 0.92
                elif type_of_currency_you_want_to_deposit == "bgn":
                    account_info.start_balance += deposit * 0.51
            elif account_info.type_of_currency == "bgn":
                if type_of_currency_you_want_to_deposit == "usd":
                    account_info.start_balance += deposit * 1.80
                elif type_of_currency_you_want_to_deposit == "eur":
                    account_info.start_balance += deposit * 1.96
    elif conf == "withdrawal":
        pin_identification = input("\nEnter your pin: ")
        if pin_identification == pin:
            sum_for_withdrawal = float(input("Enter sum for withdrawal: "))
            account_info.start_balance -= sum_for_withdrawal
    elif conf == "quit":
        break
