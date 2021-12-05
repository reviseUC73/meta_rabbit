import csv
import json

# with open('address_token.csv', 'r') as y:
#     list_ = csv.DictReader(y)
#     x = [i for i in list_]
# print(x)
# f = 0
# try:
#     print(f)
# except NameError:
#     print('1')
# else:
#     print('2')
# print('3')

# di = {'roa': 5}
# # if 'roa' in di.keys():
# #     print('yes')
# # else:
# #     print('no')
# if di.keys() == 'roa':
#     print('gg')
#
# for i in range(5):
#     print('1')
#     for j in range(5):
#         print('>>>>>>>>>>>>>>2')
#     break
dict_ = {
    'a': {"1": 'one'},
    'b': {"2": "two"},
    'c': {"3", "three"},
    'd': {"4", "four"}
}

print(list(dict_.keys()))
sw = {
    "refsfg": {
        "Password": "fasfasfafafsf2afasfa",
        "Wallet_address": "JvNOZiQbCJziMdkZVOT5hkEQrOjW2zIqP1jP6iDkhUgjbx"
    },
    "rew4vcs": {
        "Password": "f5we1f5wefwef",
        "Wallet_address": "R0XprYuebmF1GUsoE8v7kiNI4Q7XKXCw3ahsxeiEoMtNu8"
    },
    "rew": {
        "Password": "riew2545",
        "Wallet_address": "ikkatnJkXKRorQx9et4V06hrYHzVk5cISUUTS1zE0JtSGm"
    },
    "phat": {
        "Password": "admin1234",
        "Wallet_address": "Day89t5yimwcXIcJXH90ZuNfzHg7YToaGxcndv3g7vs9f2"
    },
    "jim": {
        "Password": "admin1234",
        "Wallet_address": "olU0YfQO5BwNrNsQk2dJuG2loUBydor2JgrjN7B5S3Oi60"
    },
    "gun": {
        "Password": "admin1234",
        "Wallet_address": "eiHLNp5OevTWcJ8Swd6mlLJ02ca5DTg62SRmkLbwq76bZN"
    }
}
dict1 = {'sword ': 5}
if 'gun' in sw:
    print('yep')
# with open('address_token.csv', "r") as file:
#     task = csv.DictReader(file)
#     data = [i for i in task]
# dict_name_price_token = {key['token_name']: float(key['price']) for key in data}
# print(dict_name_price_token)

# with open('address_token.csv', "r") as file:
#     task = csv.DictReader(file)
#     data = [i for i in task]
# dict_token = {key['token_name']: float(key['price']) for key in data}
# print(dict_token)

# ww = ('gg','ww','pb')
# print(ww[2])
# def check_contract(contract):
#     with open('address_token.csv', "r") as file:
#         task = csv.DictReader(file)
#         data = [i for i in task]
#     for i in data:
#         if i['contract'] == contract:
#             return i['token_name'], i['price']
# print(check_contract('0xba2ae424d960c26247dd6c32edc70b295c744c43')[0])