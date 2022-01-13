import json
import csv
from token_ import Token


class my_wallet:
    """create object by the using data from file account , wallet access to object by it will edit your data wallet
    through your address of data account and address of data wallet"""

    def __init__(self, your_address, balance):
        """
        :param your_address: string
        :param balance: int,float
        """
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

    # save and update your transaction to data_wallet
    def save(self):
        """
        update or save and dump data to data_wallet(j.son files)
        """
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

    # access your account via file data wallet json.
    def login(self, username, password):
        """
        change data object of class my_wallet by input  username, password and check
        account data if both correct data account it will change data of object by pull from data_wallet(json file)
        that correct  address that in data account(json file) and data wallet(json file)
        :param username: str
        :param password: str
        """
        with open('data_account.json', 'r') as file:
            data_account = json.load(file)
        if username in data_account and data_account[username]['Password'] == password:
            self.your_address = data_account[username]["Wallet_address"]
            with open('data_wallet.json', 'r') as file:
                data_wallet = json.load(file)
                self.balance = data_wallet[self.your_address]["Balance"]
                self.all_token = data_wallet[self.your_address]["Your_Token"]
                print(self)

    def deposit(self, values):
        """
        increase your balance of wallet and save it in data_wallet(j.son files)
        """
        self.balance += values
        self.save()

    def withdraw(self, values):
        """
        decrease your balance of wallet and save it in data_wallet(j.son files)
        """
        self.balance -= values
        self.save()

    def balance_transfer_2(self, address_transfer, values):
        """
        input address that you want to transfer if it have in data of data wallet it will increase balance (by use
        deposit method ) address_transfer and decrease your balance (use withdraw methods) but if conditions is False
        it will return the course of and errors in form string type

        :param address_transfer: str
        :param values: int, float
        :return: str
        """
        with open('data_wallet.json', 'r') as file:
            data = json.load(file)
        list_address = [i for i in data]
        if address_transfer in list_address:
            for key, val in data.items():
                if key == address_transfer:
                    wallet_transfer = my_wallet(key, data[key]['Balance'])
                    wallet_transfer.all_token = data[key]['Your_Token']
                    print(wallet_transfer)
                    if self.balance >= values:
                        wallet_transfer.deposit(values)
                        self.withdraw(values)
                        return 'yes'
                    else:
                        return 'Your balance account have not to do transactions'

        else:
            return 'Address that you want to transfer,not found addresses.'

    def import_token_(self, contract):
        """
        if contract that your input it has in address_token.csv and your wallet have not token type
        it will add type of token in your wallet and update new token type dict of your object. and save data
        in wallet data(json file) by use save method but if conditions is False
        it will return the course of and errors in form string type
        :param contract: str
        """
        list_ = []
        with open('address_token.csv', "r") as file:
            task = csv.DictReader(file)
            data = [i for i in task]
        for i in data:
            if i['contract'] == contract:
                list_.append(i['token_name'])
                list_.append(i['price'])
        if len(list_) == 0:
            return f'This contract do not available in my meta rabbit please wait to my update'
        else:
            token = Token()
            token.add_token(contract)
            if list_[0] not in self.all_token:
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
                    return 'complete'
            else:
                return 'Your account,already has a token type.'
        pass

    def buy_token_(self, name_token, price):
        """
        create object of Token
        input token name and price to buy by use increase_token method of Token class change data of object Token
        check if your balance more than or equal price that you want to buy if all condition correct
        increase amount type token that you buy and add total value of this token type (price token * amount of token)
        and decrease your balance by refer price to your buy
        but if conditions is False it will return the course of and errors in form string type
        :param name_token:
        :param price:
        :return: str
        """
        if name_token in self.all_token.keys():
            token_box = Token(name_token, 0)
            token_box.increase_token(name_token, float(price))
            print(f'You will get >>> {name_token} : {token_box.amount}')
            if float(self.balance) >= price:
                self.all_token[name_token]['Amount'] += token_box.amount
                self.all_token[name_token]["Total value"] = self.all_token[name_token]['Amount'] * token_box.price
                self.withdraw(price)
                return 'complete'
            else:
                return 'Your balance of you not enough to this Transaction.'

        else:
            return 'Your wallet does not support this type of token.' \
                   'Please use Import Token function for increase type of token support.'

    def sell_token(self, name_token, amount):
        """
        create object of Token
        input token name and amount to sell if name token that your input have in your wallet(all taken) and amount that
        you want sell less than or equal to amount that you have in my wallet it will decrease amount of token in the
        your wallet that same name wit name_token that your parameter this methods and increase your balance by the
        refer all value amount that your sell and increase by use deposit method and save in data wallet
        but if conditions is False it will return the course of and errors in form string type
        :param name_token: str
        :param amount: int,float
        :return: str
        """
        if name_token in self.all_token.keys():
            if self.all_token[name_token]['Amount'] >= amount:
                get_money = self.all_token[name_token]['Token value'] * amount
                print(f'You will get >>> {name_token} : {get_money} USDT')

                self.all_token[name_token]['Amount'] -= amount
                self.all_token[name_token]["Total value"] -= self.all_token[name_token]['Token value'] * amount
                self.deposit(get_money)
                return 'complete'
            else:
                return 'Amount token of you not enough to sell in this transaction'
        else:
            return "This token does not exist in your wallet."

    def __repr__(self):
        """represent all attributes of this class in form string """
        return f'Address : {self.your_address}\n' \
               f'Balance : {self.balance} USDT\n' \
               f'Token   : {self.all_token}'
