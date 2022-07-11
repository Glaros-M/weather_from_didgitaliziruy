from datetime import datetime
from dataclasses import dataclass
from enum import Enum

from coordinates import Coordinates

Celsius = int


# Типы погоды взяты из API погоды
class WeatherType(str, Enum):
    THUNDERSTORM = "Гроза"
    DRIZZLE = "Изморозь"
    RAIN = "Дождь"
    SNOW = "Снег"
    CLEAR = "Ясно"
    FOG = "Туман"
    CLOUDS = "Облачно"


# Подробнее изучить все начиная с ООП, заканчивая Датакласс'ами и параметрами которые передаются и могут передаваться
@dataclass(slots=True, frozen=True)
class Weather:
    temperature: Celsius
    weather_type: WeatherType
    sunrise: datetime
    sunset: datetime
    city: str


def get_weather(coordinates: Coordinates):
    """Requests weather in OpenWeather API and rerurns it"""
    return Weather(
        temperature=20,
        weather_type=WeatherType.CLEAR,
        sunrise=datetime.fromisoformat("2022-05-04 04:00:00"),
        sunset=datetime.fromisoformat("2022-05-04 20:25:00"),
        city="Moscow"
    )


