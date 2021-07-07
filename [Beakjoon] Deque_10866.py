import sys

deque = []

N = int(sys.stdin.readline())

for i in range (N):
    input = (sys.stdin.readline())

    if input[0] == ("push_front"):
        deque.insert(0,input[1]) 
     
        
    elif input[0] == ("push_back"):
        deque.append(input[1]) 
      

    elif input[0] == ("pop_front"):
        if len(deque) == 0:
            print(-1)
        else: 
            print(deque[0])
            deque.pop(input[0])

    elif input[0] == ("pop_back"):
        if len(deque) == 0:
            print(-1)
        else:
            print(deque[-1])
            deque.pop
            
    
    elif input[0] == ("size"):
        print (len(deque))

    elif input[0] == ("empty"):
        if len(deque) == 0:
            print(1)
        else:
            print(0)
    
    elif input[0] == ("front"):
        if len(deque) == 0:
            print(-1)
        else:
            print(deque[0])
        
    elif input[0] == ("back"):
        if len(deque) == 0:
            print(-1)
        else:
            print(deque[-1])



