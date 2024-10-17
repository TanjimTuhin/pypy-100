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
from art import logo
def calculator():
    print(logo) 
    num1=int(input("what's the number?: "))
    for symbol in operations:
        print(symbol)
    should_continue=True
    while should_continue:
        operation_symbol=input('Pick an operation right above:')
        num2=int(input("what's the next number?: "))

        calculation_function=operations[operation_symbol]
        answer=calculation_function(num1,num2)

        print(f'{num1}{operation_symbol}{num2}={answer}')

        if input('write "y" to continue or write "n" to new calculator')=='y':
            num1=answer
        else:
            should_continue=False
            calculator()
calculator()
