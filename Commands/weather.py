from pyowm.owm import OWM
from Commands import *
import re
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
        self._match = re.search(rf'^{self.name} (\D+)$', command)
        return bool(self._match)

    def execute(self):
        try:
            city = self._match.group(1)
            owm = OWM('6d00d1d4e704068d70191bad2673e0cc')
            mgr = owm.weather_manager()
            reg = owm.city_id_registry()
            list_of_locations = reg.locations_for(city)
            city = list_of_locations[0]
            lat = city.lat  # 55.75222
            lon = city.lon  # 37.615555
            one_call = mgr.one_call(lat, lon)
            for i in range(3):
                print(datetime.now().date() + timedelta(days=1 + i))
                print('Temperature', one_call.forecast_daily[i].temperature('celsius').get('feels_like_day', None),
                      "degrees Celsius")
                print('Wind with speed', one_call.forecast_daily[i].wind().get('speed', 0), "m/s\n")
        except IndexError and ValueError:
            print('Error! Incorrect city name')