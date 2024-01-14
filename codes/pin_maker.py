import random

def makePin() -> str:
    random1 = random.randint(1, 9) 
    random2 = random.randint(1, 9) 
    random3 = random.randint(1, 9) 
    random4 = random.randint(1, 9) 

    return f"{random1}{random2}{random3}{random4}"
