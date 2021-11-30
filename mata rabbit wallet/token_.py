import csv


class Token:
    def __init__(self, token_name='', amount=0, price=0):
        self.token_name = token_name
        self.amount = amount
        self.price = price

    @property
    def token_name(self):
        return self.__token_name

    @property
    def amount(self):
        return self.__amount

    @property
    def price(self):
        return self.__price

    @token_name.setter
    def token_name(self, other):
        if not isinstance(other, str):
            raise TypeError('a token_name is string only')
        self.__token_name = other

    @amount.setter
    def amount(self, other):
        if not isinstance(other, (int, float)):
            raise TypeError('a amount is string only')
        self.__amount = other

    @price.setter
    def price(self, other):
        if not isinstance(other, (int, float)):
            raise TypeError('a amount is string only')
        self.__price = other

    def increase_token(self, name_token, price):
        with open('address_token.csv', "r") as file:
            task = csv.DictReader(file)
            data = [i for i in task]
        dict_token = {key['token_name']: float(key['price']) for key in data}
        if name_token in dict_token:
            self.amount = price / dict_token[name_token]
            self.price = dict_token[name_token]

    def add_token(self, contract):
        """
        This method creates an object of class my_wallet by entering the contract number or address of the coin/token.
        In order for the method to return our object with the name of the coin type and the value of the coin.
        According to the actual data by storing the data in the file text csv, the function will read the address
        and use the code to modify our original object.

        :param contract:
        :return:
        """
        with open('address_token.csv', "r") as file:
            task = csv.DictReader(file)
            data = [i for i in task]
        list_contract = [i['contract'] for i in data]
        if contract in list_contract:
            for i in data:
                if i['contract'] == contract:
                    save = [i['token_name'], float(i['price'])]
                    self.token_name = save[0]
                    self.amount = 0
                    self.price = save[1]
                    break
        else:
            print('Sorry,This contract not available for systems.')

    def __repr__(self):
        return f'token_name : {self.token_name} \n' \
               f'amount     : {self.amount:.3f} \n' \
               f'price      : {self.price:.3f} \n'
