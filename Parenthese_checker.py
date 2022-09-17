from Stack import Stack

def parenthese_checker(symbolString:str) -> str:
    s = Stack() # stack object create
    balance = True
    index = 0

    while index < len(symbolString) and balance: # two condition are true
        symbol = symbolString[index]
        if symbol == "(":
            s.push(symbol)
        else:
            if s.is_empty():
                balance = False
            else:
                s.pop()

        index = index + 1

    if balance and s.is_empty():
        return True
    else:
        return False



print(parenthese_checker("((()))"))
