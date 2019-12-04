user_input = input('Say something to Mr Miyagi: ').lower()


while user_input != 'sensei, i am at peace':
    short_input = user_input[0:6]
    if 'sensei' not in short_input:
        print('You are smart, but not wise - address me as Sensei first please')
        user_input = input('Say something to Mr Miyagi: ').lower()
    elif '?' in user_input:
        print('Questions are wise, but for now. Wax on, and Wax off!')
        user_input = input('Say something to Mr Miyagi: ').lower()
    elif 'block' in user_input:
        print('Remember, best block, not to be there...')
        user_input = input('Say something to Mr Miyagi: ').lower()
    else:
        print('Do not lose focus. Wax on. Wax off.')
        user_input = input('Say something to Mr Miyagi: ').lower()
print('Sometimes, what heart know, head forget')


#
# user_input = 'none'
# while user_input != 'sensei, i am at peace':
#     user_input = input('Say something to Mr Miyagi: ').lower()
#     short_input = user_input[0:6]
#     if 'sensei' not in short_input:
#         print('You are smart, but not wise - address me as Sensei first please')
#     elif '?' in user_input:
#         print('Questions are wise, but for now. Wax on, and Wax off!')
#     elif 'block' in user_input:
#         print('Remember, best block, not to be there...')
#     else:
#         print('Do not lose focus. Wax on. Wax off.')
#
# print('Sometimes, what heart know, head forget')
