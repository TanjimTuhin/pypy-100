# Write your code below this line 👇
def prime_checker (number):
    prime=True
    if number < 2:
        prime= False
    for i in range (2, int (number ** 0.5) + 1):
        if number % i == 0:
            prime =False
            
        prime= True
        
    if prime: 
        print('prime number')
    else:
        print('not a prime number')

# Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input()) # Check this number
prime_checker(number=n)