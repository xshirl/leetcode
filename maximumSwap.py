def maximumSwap(num):
    A = list(str(num))
    ans = A[:]
    for i in range(len(A)):
        for j in range(i+1, len(A)):
            A[i], A[j] = A[j], A[i]
            if A > ans:
                ans = A[:]
            A[i], A[j] = A[j], A[i]

    return int("".join(ans))


# https://leetcode.com/problems/maximum-swap/submissions/

def maximumSwap2(self, num: int) -> int:
    if num < 10:
        return num

    num_lst = [int(n) for n in list(str(num))]
    idx_dict = {n: i for i, n in enumerate(num_lst)}

    for cur_i, n in enumerate(num_lst):
        for d in range(9, 0, -1):
            if d > n and d in idx_dict and idx_dict[d] > cur_i:
                num_lst[cur_i], num_lst[idx_dict[d]
                                        ] = num_lst[idx_dict[d]], num_lst[cur_i]
                return int(''.join(map(str, num_lst)))
            if d <= n:
                break
    return num
