alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
             'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar(). 
def caesar(end_text, shift_amount , cipher_direction):
    cipher_result=''
    if cipher_direction=='decode':
            shift_amount *= -1
    for letter in end_text:
        position=alphabet.index(letter)
           
        new_position=position+shift_amount
        cipher_result+=alphabet[new_position]
    print(f'The {cipher_direction}d text is {cipher_result}')

caesar(end_text=text, shift_amount=shift, cipher_direction=direction)