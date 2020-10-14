import collections


def hashkey(string):
    arr = [0] * 26
    for s in string:
        arr[ord(s) - ord('a')] = 1
    return tuple(arr)


def groupAnagrams(string):
    groups = collections.defaultdict(list)
    for s in string:
        groups[hashkey(s)].append(s)
    return tuple(groups.values())


print(groupAnagrams(['abc', 'bcd', 'cba', 'cbd', 'efg']))
