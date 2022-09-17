def binary_to_decimal(binNum:int) -> int:
    binNum = str(binNum)
    p_cout = len(binNum)
    mylist = []

    for i in binNum:
        p_cout = p_cout - 1
        dec = int(i) * (2 ** p_cout)
        mylist.append(dec)

    decimalNum = 0

    while len(mylist) > 0:
        decimalNum = decimalNum + mylist.pop()

    return decimalNum
