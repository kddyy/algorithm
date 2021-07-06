import sys
Stack = []

N = int(sys.stdin.readline())

for i in range (N):
    input = sys.stdin.readline().split()

    if input[0] == ("push"):
        Stack.append(input[1])

    elif input[0] == ("pop"):
        if len(Stack) == 0:
            print(-1)
        else:
            print(Stack[-1])
            Stack.pop()[-1]
    
    elif input[0] == ("size"):
        print(len(Stack))

    elif input[0] == ("empty"):
        if len(Stack) == 0:
            print(1)
        else :
            print(0)
    
    elif input[0] == ("top"):
        if len(Stack) ==0:
            print(-1)
        else:
            print(Stack[-1])
        

