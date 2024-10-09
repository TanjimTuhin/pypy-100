target=int(input())

for both in range(1,int(target+1)):
    if both % 3 == 0 and both % 5 == 0:
         print("FizzBuzz")
    elif both % 3 == 0:
         print("Fizz")
    elif both % 5 == 0:
         print("Buzz")
    else:
         print(both)
