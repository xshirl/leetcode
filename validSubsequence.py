def isValidSubsequence(array, sequence):
    # Write your code here.
    i = 0
    j = 0
    count = 0
    if len(array) < len(sequence):
        return False
    while i < len(array) and j < len(sequence):
        if array[i] == sequence[j]:
            count += 1
            if count == len(sequence):
                return True
            else:
                i += 1
                j += 1
        else:
            i += 1

    return False
