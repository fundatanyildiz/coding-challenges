def romanToInt(s):
    """
    :type s: str
    :rtype: int
    """
    sum = 0
    map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    # I placed before IV and IX->> means subtraction X-I=9
    # X placed before XL and XC->> 40 and 90
    # C placed before CD and CM->> 400 and 900
    # usually written largest to smallest from left to right except above cases.
    r = s[::-1]

    for index, i in enumerate(r):
        if index == 0:
            sum += map[i]
        elif map[i] >= map[r[index - 1]]:
            sum += map[i]
        elif map[i] < map[r[index - 1]]:
            sum -= map[i]
    return sum


s = "IV"
print(romanToInt(s))
