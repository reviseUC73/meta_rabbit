import json
import random


class Account:
    """keep data of account so that thing bring you to your wallet by using address as an intermediary
     between user account with user of wallet"""

    def __init__(self, username, password, address):
        """determine attributes of this class"""
        self.username = username
        self.password = password
        self.address = address

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, other):
        if not isinstance(other, str):
            raise TypeError('username must to string')
        self.__username = other

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, other):
        if not isinstance(other, str):
            raise TypeError('password must to string')
        self.__password = other

    def build_address(self):
        """change self.address attribute of object to number and character big and small by all together of them
        are 46 cheater and dump it to self.address object"""
        list_number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        list_ = []
        address = ''
        for i in range(65, 91):
            list_.append(chr(i))
        for i in range(97, 123):
            list_.append(chr(i))
        for j in list_number:
            list_.append(j)
        for i in range(46):
            address += random.choice(list_)
        self.address = address

    def create_account(self):
        """
        if your attribute password have numbers of characters more than or equal to 8  and it not all number only
        and username have not in data_account json file (key)
        it will create your account by keep data of account ,password, your_address with is attribute of class
        in file data account and create object of class my_wallet by attributes have defeat is
        self.your_address of object my_wallet is same self.address of this class(Account) , self.balance will be 0
        and  self.token will be dict empty and save all together of object my_wallet in file wallet_data
        if condition up there errors it will return the course of and errors in form string type.
        """
        if len(self.password) >= 8 and not self.password.isnumeric():

            self.build_address()

            new_account = {
                self.username: {
                    'Password': self.password,
                    'Wallet_address': self.address
                }
            }
            new_wallet_data = {
                self.address: {
                    'Balance': 0,
                    'Your_Token': {}
                }
            }
            try:
                with open("data_account.json", 'r') as file_w:  # read
                    data_account = json.load(file_w)

            except FileNotFoundError:

                with open("data_account.json", 'w') as file_ad:  # new
                    json.dump(new_account, file_ad, indent=4)
                with open("data_wallet.json", 'w') as file_wd:  # new
                    json.dump(new_wallet_data, file_wd, indent=4)
                print('complete')
                return f'complete'
            else:
                with open("data_wallet.json", "r") as file_a:  # read
                    data_wallet = json.load(file_a)

                if self.username in data_account.keys():
                    print('This username has been used')
                    return 'nope_have'

                elif self.username not in data_account or self.address not in data_account['Wallet_address']:
                    data_account.update(new_account)
                    data_wallet.update(new_wallet_data)
                    with open('data_account.json', 'w') as file:
                        json.dump(data_account, file, indent=4)
                    with open('data_wallet.json', 'w') as file:
                        json.dump(data_wallet, file, indent=4)
                    print('complete')
                    return f'complete'
        else:
            print('Your password have to include number more than one and there must be '
                  'more than 6 numbers and letters combined')
            return f'nope_less'

    def __repr__(self):
        """determine attributes of this class"""
        return f'username : {self.username}' \
               f'password : {self.password}' \
               f'address  : {self.password}'
