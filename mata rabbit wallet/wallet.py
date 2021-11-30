import json
import csv

from token_ import Token


def check_contract(contract):
    with open('address_token.csv', "r") as file:
        task = csv.DictReader(file)
        data = [i for i in task]
    for i in data:
        if i['contract'] == contract:
            return i['token_name'], i['price']


class my_wallet:
    """create object by use data from file account , wallet access to object  """

    def __init__(self, your_address, balance):
        self.your_address = your_address
        self.balance = balance
        self.all_token = {}

    @property
    def your_address(self):
        return self.__your_address

    @your_address.setter
    def your_address(self, other):
        if not isinstance(other, str):
            raise TypeError('it must to string')
        self.__your_address = other

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, other):
        if not isinstance(other, (float, int)):
            raise TypeError('it must to float or integer')
        self.__balance = other

    @property
    def all_token(self):
        return self.__all_token

    @all_token.setter
    def all_token(self, other):
        if not isinstance(other, dict):
            raise TypeError('it must to class Wallet')
        self.__all_token = other

    def save(self):
        with open('data_wallet.json', 'r') as file:
            data = json.load(file)
        for key, val in data.items():
            if key == self.your_address:
                update_wallet_data = {
                    self.your_address: {
                        'Balance': self.balance,
                        'Your_Token': self.all_token
                    }
                }
                data.update(update_wallet_data)
                break
        with open('data_wallet.json', 'w') as file:
            json.dump(data, file, indent=4)

    def deposit(self, values):
        self.balance += values
        self.save()

    def withdraw(self, value):
        self.balance -= value
        self.save()

    def balance_transfer(self, address_transfer, values):
        with open('data_wallet.json', 'r') as file:
            data = json.load(file)
        list_address = [i for i in data]
        if address_transfer in list_address:
            for key, val in data.items():
                wallet_transfer = my_wallet(key, data[key]['Balance'])
                wallet_transfer.all_token = data[key]['Your_Token']
                print(f'Convert to >>> {wallet_transfer.your_address}\n')

                if self.balance >= values:
                    wallet_transfer.deposit(values)
                    self.withdraw(values)
                    print(self)
                else:
                    print('Your balance account have not to do transactions')
                break
        else:
            print('Address that you want to transfer,not found addresses.')

    def import_token(self, contract):
        token = Token()
        token.add_token(contract)
        if check_contract(contract)[0] not in self.all_token:
            if token.token_name != '':
                new_token = {
                    token.token_name: {
                        'Amount': token.amount,
                        'Token value': token.price,
                        'Total value': token.amount * token.price
                    }
                }
                self.all_token.update(new_token)
                self.save()
        else:
            print('Your account,already has a token type.')
        pass

    def login(self, username, password):
        """
        create object of class my_wallet by use data from data_account
        :param username: str
        :param password: str
        :return:
        """
        with open('data_account.json', 'r') as file:
            data_account = json.load(file)
        if username in data_account and data_account[username]['Password'] == password:
            self.your_address = data_account[username]["Wallet_address"]
            with open('data_wallet.json', 'r') as file:
                data_wallet = json.load(file)
                self.balance = data_wallet[self.your_address]["Balance"]
                self.all_token = data_wallet[self.your_address]["Your_Token"]

    def buy_token(self, name_token, price):
        if name_token in self.all_token.keys():
            token_box = Token(name_token, 0)
            token_box.increase_token(name_token, price)
            print(f'You will get >>> {name_token} : {token_box.amount}')
            if input('Confirm Transaction (Y or N) >>>').upper() == "Y":
                if self.balance >= price:
                    self.all_token[name_token]['Amount'] += token_box.amount
                    self.all_token[name_token]["Total value"] = self.all_token[name_token]['Amount'] * token_box.price
                    self.withdraw(price)
                else:
                    print('Your balance of you not enough to this Transaction.')
            else:
                print('This order is canceled')
        else:
            print('Your wallet does not support this type of token.\n'
                  'Please use Import Token function for increase type of token support.')

    def sell_token(self, name_token, amount):
        if name_token in self.all_token.keys():
            if self.all_token[name_token]['Amount'] >= amount:
                get_money = self.all_token[name_token]['Token value'] * amount
                print(f'You will get >>> {name_token} : {get_money} USDT')
                if input('Confirm Transaction (Y or N) >>>').upper() == "Y":
                    self.all_token[name_token]['Amount'] -= amount
                    self.deposit(get_money)
                else:
                    print('This order is canceled')
            else:
                print('Amount token of you not enough to sell in this transaction')

    def __repr__(self):
        return f'Address : {self.your_address}\n' \
               f'Balance : {self.balance} USDT\n' \
               f'Token   : {self.all_token}'
