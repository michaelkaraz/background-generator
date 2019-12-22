# def sum(arg):
#     total = 0
#     for val in arg:
#         total += val
#     return total
name = input('User Name: ')
password = input('Password: ')

print(f'Your user name is {name}\nYour password {len(password) * "*"} is {len(password)} charactors')