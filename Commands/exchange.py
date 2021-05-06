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
        return 'Currency conversion into Russian rubles\nFor example: EXCHANGE 100 USD\n'

    def can_execute(self, command: str) -> bool:
        self._match = re.search(rf'^{self.name} (\d+) (\w\w\w)$', command)
        return bool(self._match)

    def execute(self):
        try:
            currency_code = self._match.group(2)
            currency_value = int(self._match.group(1))
            reqest = requests.get('https://www.cbr.ru/currency_base/daily/')
            reqest.encoding = 'utf8'
            list_parsing = re.findall(r'(\w+)', reqest.text)
            currency_code_parsing: int = list_parsing.index(currency_code)
            currencies_parsing = float(list_parsing[currency_code_parsing + 10] + '.' + list_parsing[currency_code_parsing + 11]) / float(list_parsing[currency_code_parsing + 3])
            result = round(currencies_parsing * currency_value, 2)
            print(currency_value, currency_code, '=', result, 'RUB')
        except:
            print('Error!')