"""
1에서 100까지 출력
3의 배수는 Fizz 출력
5의 배수는 Buzz 출력
3과 5의 공배수는 FizzBuzz 출력
"""

#1

for i in range(1,101):
    print(i)

#2

for i in range(1,101):
    if i % 3 == 0:
        print("Fizz")
    else:
        print(i)


#3
for i in range(1,101):
    if i % 5 == 0:
        print("Buzz")
    else:
        print(i)


#4
for i in range(1,101):
    if i % 3 and i % 5:
        print("pizzBuzz")
    else:
        print(i)

#all 
for i in range (1,101):
    if i % 3 == 0:
        print("Fizz")
    
    elif i % 5 == 0:
        print("Buzz")
    
    elif i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")

    else:
        print(i)