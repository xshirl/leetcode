def staircase(n):
    if n <= 1:
        return 1
    return staircase(n-1) + staircase(n-2)


def staircase2(n):
    prev = 1
    prevprev = 1
    for i in range(2, n+1):
        curr = prev + prevprev
        prevprev = prev
        prev = curr
    return curr


print(staircase2(5))
