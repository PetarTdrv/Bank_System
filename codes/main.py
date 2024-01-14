import account_info 
from pin_maker import makePin
from iban_maker import makeIban

iban: str = makeIban()
pin: str = makePin()

print(f"\nOwner of card is: {account_info.owner}")
print(f"Iban of card is: {iban}")
print(f"PIN of card is: {pin}")
