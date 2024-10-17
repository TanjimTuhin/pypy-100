#add
def add(n1,n2):
    """This funtion is used for addition"""
    return n1+n2

#sub
def sub(n1,n2):
    """This function is used for subtraction"""
    return n1-n2

#mul
def mul(n1,n2):
    """This function is used for multiplication"""
    return n1*n2

#div
def div(n1,n2):
    """This function is used for division"""
    return n1/n2

operations={
    "+":add,
    "-":sub,
    "*":mul,
    "/":div
}

num1=int(input("what's the first number?: "))
num2=int(input("what's the second number?: "))

for symbol in operations:
    print(f"{num1} {symbol} {num2} = {operations[symbol]})