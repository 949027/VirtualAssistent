from Commands import *
import re
from pyowm.owm import OWM
from pyowm.utils.config import get_default_config
from datetime import datetime, timedelta


class Weather(AbstractCommand):

    @property
    def name(self) -> str:
        return 'WEATHER'

    @property
    def help(self) -> str:
        return 'The weather forecast for tomorrow\nFor example: WEATHER Tomsk\n'

    def can_execute(self, command: str) -> bool:
        self._match = re.search(rf'^{self.name} (\D+[A-Za-z])$', command)
        return bool(self._match)

    def execute(self):
        city = self._match.group(1)
        config_dict = get_default_config()
        config_dict['language'] = 'en'
        owm = OWM('6d00d1d4e704068d70191bad2673e0cc', config_dict)
        reg = owm.city_id_registry()
        mgr = owm.weather_manager()
        #проверка на полное совпадение
        try:
            list_of_locations = reg.locations_for(city)
            city = list_of_locations[0]
        except:
            #проверка на частичное совпадение
            try:
                list_of_tuples = reg.ids_for(city, matching='like')
                city = list_of_tuples[0][1]
            except IndexError:
                print('No object with this name was found\n')
                return ()
            #вывод списка с вариантами
            if len(list_of_tuples) > 1:
                for i in range(0, len(list_of_tuples)):
                    print(i + 1, list_of_tuples[i][1:3])
                #выбор пользователя и проверка
                try:
                    select = int(input('\nSeveral matches were found. Enter a suitable number\n--> '))
                    city = list_of_tuples[select - 1][1]
                    list_of_locations = reg.locations_for(city)
                    city = list_of_locations[0]
                    if select < 1:
                        print('Incorrected input\n')
                        return ()
                except:
                    print('Incorrected input\n')
                    return ()

        print('Wait forecast for', city.name, '...\n')
        lat = city.lat
        lon = city.lon
        one_call = mgr.one_call(lat, lon)
        for i in range(3):
            print(datetime.now().date() + timedelta(days=1 + i))
            print('Wind:', one_call.forecast_daily[i].wind().get('speed', 0), 'm/s\n'
                                                                              'Cloudes:',
                  one_call.forecast_daily[i].detailed_status, '\nDay temperature:',
                  one_call.forecast_daily[i].temperature('celsius').get('feels_like_day', None),
                  'degrees Celsius', '\nNight temperature:',
                  one_call.forecast_daily[i].temperature('celsius').get('feels_like_night',
                                                                        None), "degrees Celsius\n")