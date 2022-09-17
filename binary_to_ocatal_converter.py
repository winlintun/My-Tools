def binary_to_octal(binNum:int) -> int:
    binNum = str(binNum)
    p_cout = len(binNum)
    mylist = []

    # first we neet to convert decimal
    for i in binNum:
        p_cout = p_cout - 1
        dec = int(i) * (2 ** p_cout)
        mylist.append(dec)

    decimalNum = 0

    while len(mylist) > 0:
        decimalNum = decimalNum + mylist.pop()


    # decimal to octal
    # function call now
    octNumber = decimal_to_octal_converter(decimalNum)
    return octNumber
  
  '''
def decimal_to_octal_converter(decimalNum:int) -> str:
  mylist = []

  while decimalNum > 0:
    rem = decimalNum % 8
    mylist.append(rem)
    decimalNum //= 8

  octString = ''
  while len(mylist) > 0:
    octString += str(mylist.pop())

  return octString
  
  
  '''
