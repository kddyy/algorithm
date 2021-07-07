import sys 

N = int(sys.stdin.readline())

queue = [] 

for i in range (N):
    ipt = sys.stdin.readline().split()


    if ipt[0] == ("push"):
        queue.append(ipt[1]) 
        

    elif ipt[0] == ("pop"):
        if len(queue) != 0:
            print(queue.pop())
        else:
            print(-1)

    elif ipt[0] == ("size"):
        print(len(queue))

    elif ipt[0] == ("empty"):
        if len(queue) == 0 :
            print (1)
        else :
            print(0)

    elif ipt[0] == ("front"):
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[len(queue)-1])

    elif ipt[0] == ("back"):
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])






