from collections import Counter


def mode(root):
    c = Counter(root)
    mode = 0
    num = 0
    res = []
    for key, value in c.items():
        if value > mode:
            mode = value
            num = key
    res.append(num)

    return res


print(mode([1, 2, 2, 2, 3, 3]))
