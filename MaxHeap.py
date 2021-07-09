import sys
heap = []
N = int(sys.stdin.readline())
for i in range (N):
    X = int(sys.stdin.readline())
    if X == 0:
        if not heap:
            print(0)
        else:
            print(max(heap))
            heap = [heap.pop(heap.index(max(heap)))]

    else: 
        heap.append(X)


