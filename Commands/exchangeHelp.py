from Commands import *
import re

class Exchange_Help(AbstractCommand):
    @property
    def name(self) -> str:
        return 'EXCHANGE HELP'

    @property
    def help(self) -> str:
        return 'Information on currency codes\n'

    def can_execute(self, command: str) -> bool:
        self._match = re.search(rf'^{self.name}$', command)
        return bool(self._match)

    def execute(self):
        info = 'AMD	Armenia Dram\nAUD	Australian Dollar\nAZN	Azerbaijan Manat\nBGN	Bulgarian lev\nBRL	Brazil Real\n' \
               'BYN	Belarussian Ruble\nCAD	Canadian Dollar\nCHF	Swiss Franc\nCNY	China Yuan\nCZK	Czech Koruna\nDKK	Danish Krone\n' \
               'EUR	Euro\nGBP	British Pound Sterling\nHKD	Hong Kong Dollar\nHUF	Hungarian Forint\nINR	Indian Rupee\nJPY	Japanese Yen\n' \
               'KGS	Kyrgyzstan Som\nKRW	South Korean Won\nKZT	Kazakhstan Tenge\nMDL	Moldova Lei\nNOK	Norwegian Krone\nPLN	Polish Zloty\n' \
               'RON	Romanian Leu\nRUB	Russian rubles\nSEK	Swedish Krona\nSGD	Singapore Dollar\nTJS	Tajikistan Ruble\nTMT	New Turkmenistan Manat\n' \
               'TRY	Turkish Lira\nUAH	Ukrainian Hryvnia\nUSD	US Dollar\nUZS	Uzbekistan Sum\nXDR	SDR\nZAR	S.African Rand\n'
        print(info)