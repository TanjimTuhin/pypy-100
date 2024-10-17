#Function with output

def format_name(f_name,l_name):
    formatted_f_name=f_name.title()
    formatted_l_name=l_name.title()

    return f'Your name is {formatted_f_name} {formatted_l_name}'


print(format_name(input('what is your first name:'),input('what is your last name:')))