def plusOne(digits):
    string = ""
    for digit in digits:
        string += digit
    num = int(string)
    sumNum = num + 1
    sumStr = str(sumNum)
    arr = [i for i in sumStr]
    return arr
