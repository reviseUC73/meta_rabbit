# from account import Account
# from wallet import my_wallet
#
# print('Main menu\n'
#       '1. register\n'
#       '2. login\n')
# num = int(input('enter menu number >> '))
# username = input('username : ')
# password = input('password : ')
# print('')
# if num == 1:
#     user1 = Account(username, password, '')
#     user1.create_account()
# elif num == 2:
#     user_wallet = my_wallet('', 0)
#     user_wallet.login(username, password)
#     if user_wallet.your_address != '':
#         print(user_wallet)
#         print('')
#         print('Menu choice\n'
#               '1. Deposit\n'
#               '2. Withdraw\n'
#               '3. Transfer\n'
#               '4. Import Token\n'
#               '5. Buy Token\n'
#               '6. Sell Token\n'
#               ' Exit \n')
#
#         while True:
#             x = input('Choice >> ')
#             if x == '1':
#                 money = float(input('Amount to deposit : '))
#                 user_wallet.deposit(money)
#                 print(user_wallet)
#
#             elif x == '2':
#                 money = float(input('Amount to withdraw : '))
#                 user_wallet.withdraw(money)
#                 print(user_wallet)
#
#             elif x == '3':
#                 to_address = input('Enter address to transfer >>> ')
#                 money = float(input('Balance money : '))
#                 user_wallet.balance_transfer(to_address, money)
#             elif x == '4':
#                 address = input('input_contract >>> ')
#                 user_wallet.import_token_(address)
#                 print('')
#                 print(user_wallet)
#                 pass
#             elif x == '5':
#                 name_token = input('Name token: ')
#                 price = float(input('Price : '))
#                 user_wallet.buy_token(name_token, price)
#                 print('')
#                 print(user_wallet)
#             elif x == '6':
#                 name_token = input('Name token: ')
#                 amount = float(input('Amount : '))
#                 user_wallet.sell_token(name_token, amount)
#                 print('')
#                 print(user_wallet)
#             elif x.lower() == 'exit':
#                 break
#
#     else:
#         print('your username or password is wrong please check it again')
