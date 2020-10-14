
def rotateString(A, B):
    res = []

    for i in range(1, len(A)):
        res.append(A[i])
    res.append(A[0])
    if "".join(res) == B:
        return True
    else:
        return rotateString(res, B)
    return False


print(rotateString("abcde", "abced"))


class Solution(object):
    def rotateString(self, A, B):
        return any(A[i:] + A[:i] == B for i in range(len(A))) or A == B == ""
