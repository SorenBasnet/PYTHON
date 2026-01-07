

def binarySearch(arr: list, key: int): # arr is sorted btw
    left: int = 0
    right: int = len(arr) - 1
    mid: int = 0

    while (left <= right): 
        mid = left + (right-left) // 2

        if(arr[mid] > key):
            right = mid - 1

        elif (arr[mid] < key): 
            left = mid + 1

        else: 
            return True
        
    return False


arr = [1,2,3,4,6,7,8,9]
print(binarySearch(arr, 8))

