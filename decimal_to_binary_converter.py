def decimal_to_binary_converter(decimalNum:int) -> str:
    """
    668/2 = 334 -> 0
    334/2 = 167 -> 0
    167/2 = 83.5 -> 1
    83/2 = 41.5 -> 1
    41/2 = 20.5 -> 1
    20/2 = 10 -> 0
    10/2 = 5 -> 0
    5/2 = 2.5 -> 1
    2/2 = 1 -> 0
    1/2 = 0.5 -> 1

    ans = 1010011100

    စားလို့ ပြတ်တယ်ဆိုရင် 0
    စားလို့ မပြတ်ဘူးဆိုရင် 1
    """

    mylist = []

    while decimalNum > 0:
        rem = decimalNum % 2 # remainder
        mylist.append(rem)
        decimalNum = decimalNum // 2

    binString = ''
    while len(mylist) > 0:
        binString = binString + str(mylist.pop())

    return binString
