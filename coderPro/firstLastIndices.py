class Solution:
    def getRange(self, arr, target):
        first = self.binarySearchIterative(arr, 0, len(arr)-1, target, True)
        last = self.binarySearchIterative(arr, 0, len(arr) - 1, target, False)
        return [first, last]

    def binarySearchIterative(self, arr, low, high, target, findFirst):
        while True:
            if high < low:
                return -1
            mid = low + (high - low) // 2
            if findFirst:
                if(mid == 0 or target > arr[mid-1]) and arr[mid] == target:
                    return mid
                if target > arr[mid]:
                    low = mid + 1
                else:
                    high = mid - 1
            else:
                if (mid == len(arr)-1 or target < arr[mid+1]) and arr[mid] == target:
                    return mid
                elif target < arr[mid]:
                    high = mid - 1
                else:
                    low = mid + 1

    def binarySearch(self, arr, low, high, target, findFirst):
        if high < low:
            return - 1
        mid = low + (high - low)//2
        if findFirst:
            if (mid == 0 or target > arr[mid-1]) and arr[mid] == target:
                return mid
            if target > arr[mid]:
                return self.binarySearch(arr, mid+1, high, target, findFirst)
            else:
                return self.binarySearch(arr, low, mid-1, target, findFirst)
        else:
            if (mid == len(arr)-1 or target < arr[mid+1]) and arr[mid] == target:
                return mid
            if target < arr[mid]:
                return self.binarySearch(arr, low, mid-1, target, findFirst)
            else:
                return self.binarySearch(arr, mid+1, high, target, findFirst)


print(Solution().getRange([1, 3, 3, 5, 7, 8, 9, 9, 15], 9))
