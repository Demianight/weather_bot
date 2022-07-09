from subprocess import DETACHED_PROCESS
from xml.dom import NotFoundErr
from pyowm import OWM
from pyowm.utils.config import get_default_config
from pyowm.commons.exceptions import NotFoundError


class Weather:

    def __init__(self, user_city='moscow', temperature=None, detailed_weather=None):
        self.user_city = user_city
        self.temperature = temperature
        self.detailed_weather = detailed_weather

    config_dict = get_default_config()
    config_dict['language'] = 'ru' 
    
    def create_user_weather(self):
        try:
            owm = OWM('5fdd4f577868060bfa28fd495962d8ec')
            mgr = owm.weather_manager()
            observation = mgr.weather_at_place(self.user_city)
            user_weather = observation.weather
        except NotFoundError:
            return False
        return user_weather

    def get_temperature(self):
        temperature = self.create_user_weather().temperature('celsius')['temp']
        return round(temperature)

    def get_detailed_weather(self):
        detailed_weather = self.create_user_weather().detailed_status
        return detailed_weather

    def get_pressure(self):
        pressure = self.create_user_weather().barometric_pressure()['press']
        return pressure / 1000
