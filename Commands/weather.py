from pyowm.owm import OWM
from Commands import *
import re


class Weather(AbstractCommand):

    @property
    def name(self) -> str:
        return 'WEATHER'

    @property
    def help(self) -> str:
        return 'The weather forecast for tomorrow\nFor example: WEATHER Tomsk\n'

    def can_execute(self, command: str) -> bool:
        self._match = re.search(rf'^{self.name} (\w+)$', command)
        return bool(self._match)

    def execute(self):
        try:
            city = self._match.group(1)
            owm = OWM('57843cbd3a57759ff214e2ac9fae419a')
            mgr = owm.weather_manager()
            reg = owm.city_id_registry()
            list_of_locations = reg.locations_for(city)
            city = list_of_locations[0]
            lat = city.lat  # 55.75222
            lon = city.lon  # 37.615555
            one_call = mgr.one_call(lat, lon)

            print('Temperature tomorrow', one_call.forecast_daily[0].temperature('celsius').get('feels_like_day', None),
                  "degrees Celsius")
            print('Wind with speed', one_call.forecast_daily[0].wind().get('speed', 0), "m/s")
        except IndexError:
            print('Error! Incorrect city name')