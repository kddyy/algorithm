import sys
import heapq

N = int(sys.stdin.readline())
heap = []

for i in range(N):
    input = int(sys.stdin.readline())
    if input == 0:
        try:
            print(-1 * heapq.heappop(heap))
        except:
            print(0)
    else:
        heapq.heappush(heap,-input) 



