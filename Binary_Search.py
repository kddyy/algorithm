
data = list(map(int,input().split()))
target = int(input())
def binary_search(target, data):
    data.sort()
    start = 0
    end = len(data) - 1

    while start <= end:
        mid = (start + end) // 2

        if data[mid] == target:
            return mid 
        elif data[mid] < target:
            start = mid + 1
        else:
            end = mid -1

    print(None)

