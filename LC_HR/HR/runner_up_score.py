if __name__ == '__main__':
    n = int(input())
    arr = list(dict.fromkeys(map(int, input().split())))


    if len(arr) == 1:
        print(arr[0])

    else:
        print(arr[len(arr)-1])







