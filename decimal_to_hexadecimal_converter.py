def decimal_to_hexadecimal(decimalNum:int) -> str:
    """
    hexadecimal = [0,1,2,3,4,5,6,7,8,9,10=A,11=B,12=C,13=D,14=E,15=F]

    668/16 = 41.75 -> 0.75 * 16 = 12
    41/16 = 2.5625 -> 0.5625 * 16 = 9
    2/16 = 0.125 -> 0.125 * 16 = 2
    0/16 = 0

    ans = 2912 -> 29C

    စားလို့ရတဲ့အကြွင်းကို 16 နဲ့မြှောက်
    """

    mylist = []

    hexa = {10:"A", 11:'B', 12:"C", 13:"D", 14:"E", 15:"F"}

    while decimalNum > 0:
        rem = decimalNum % 16

        if rem > 9:
            for key, val in hexa.items():
                if rem == key:
                    mylist.append(val)
        else:
            mylist.append(rem)

        decimalNum //= 16

    hexaString = ''

    while len(mylist) > 0:
        hexaString += str(mylist.pop())

    return hexaString
