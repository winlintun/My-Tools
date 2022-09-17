def decimal_to_octal_converter(decimalNum:int) -> str:
    """
    668/8 = 83.5 -> 0.5 * 8 = 4
    83/8 = 10.375 -> 0.375 * 8 = 3
    10/8 = 1.25 -> 0.25 * 8 = 2
    1/8 = 0.125 = 0.125 * 8 = 1

    ans = 1234

    စားလို့ရတဲ့အကြွင်းကို 8 နဲ့မြှောက်
    """

    mylist = []

    while decimalNum > 0:
        rem = decimalNum % 8
        mylist.append(rem)

        decimalNum //= 8

    octString = ''
    while len(mylist) > 0:
        octString += str(mylist.pop())

    return octString
