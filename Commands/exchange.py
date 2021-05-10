from Commands import *
import requests
import re


class Exchange(AbstractCommand):
    def __init__(self):
        self._match = None

    @property
    def name(self) -> str:
        return 'EXCHANGE'

    @property
    def help(self) -> str:
        return 'Currency Converter\nFor example: EXCHANGE 100.00 USD RUB\n'

    def can_execute(self, command: str) -> bool:
        self._match = re.search(rf'^{self.name} (\d+.\d\d) (\w\w\w) (\w\w\w)$', command)
        return bool(self._match)

    def execute(self):
        try:
            money_code_1 = (self._match.group(2))
            money_code_2 = (self._match.group(3))
            value = float(self._match.group(1))
            reqest = requests.get('https://www.cbr.ru/currency_base/daily/')
            reqest.encoding = 'utf8'
            list_parsing = re.findall(r'([A-Z0-9]+)', reqest.text)

            if money_code_1 != 'RUB':
                index_code_1: int = list_parsing.index(money_code_1)
                currencies_1 = float(list_parsing[index_code_1 + 2] + '.' + list_parsing[index_code_1 + 3]) / float(
                    list_parsing[index_code_1 + 1])
            else:
                currencies_1 = 1

            if money_code_2 != 'RUB':
                index_code_2: int = list_parsing.index(money_code_2)
                currencies_2 = float(
                    list_parsing[index_code_2 + 2] + '.' + list_parsing[index_code_2 + 3]) / float(
                    list_parsing[index_code_2 + 1])
            else:
                currencies_2 = 1

            result = round(currencies_1 * value / currencies_2, 2)
            if result < 0.01:
                print('The result is too small. Increase the value')
            else:
                print(value, money_code_1, '=', result, money_code_2)
        except:
            print('Error! Check the entered currency codes.\nFor information on currency codes enter "EXCHANGE HELP"')