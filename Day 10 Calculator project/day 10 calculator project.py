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
for symbol in operations:
    print(symbol)
operation_symbol=input('Pick an operation right above:')
num2=int(input("what's the second number?: "))

calculation_function=operations[operation_symbol]
answer=calculation_function(num1,num2)

print(f'{num1}{operation_symbol}{num2}={answer}')

operation_symbol=input('Pick an another operation:')
num3=int(input("what's the second number?: "))
calculation_function=operations[operation_symbol]
second_answer=calculation_function(answer,num3)
print(f'{answer}{operation_symbol}{num3}={second_answer}')