import random
from account_info import country

def makeIban() -> str:
    random1: int = random.randint(1, 9)
    random2: int = random.randint(1, 9)
    random3: int = random.randint(1, 9)
    random4: int = random.randint(1, 9)
    random5: int = random.randint(1, 9)

    iban: str = ""
    match country:
        case "bg":
            iban = f"BG80BNBG96611020345678{random1}{random2}{random3}{random4}{random5}"
        case "de":
            iban = f"DE89370400440532013000{random1}{random2}{random3}{random4}{random5}"
        case "fr":
            iban = f"FR1420041010050500013M{random1}{random2}{random3}{random4}{random5}"
        case "it":
            iban = f"IT60123456789012345678{random1}{random2}{random3}{random4}{random5}"
        case "gb":
            iban = f"GB29NWBK60161331926819{random1}{random2}{random3}{random4}{random5}"
        case _:
            iban = f"EU29NWBK60161331926819{random1}{random2}{random3}{random4}{random5}"

    return iban
