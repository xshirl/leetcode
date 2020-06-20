def romanToInt(s):
    num = 0
    roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    for idx, char in enumerate(s):
        this_num = roman[char]
        if idx < len(s) - 1:
            next_num = roman[s[idx+1]]
        else:
            next_num = 0
        if this_num < next_num:
            num -= this_num
        else:
            num += this_num
    return num


print(romanToInt("IV"))

# https://leetcode.com/problems/roman-to-integer/
