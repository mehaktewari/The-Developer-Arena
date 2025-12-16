from .weather_api import WeatherAPI
from .weather_parser import parse_current, parse_forecast
from .weather_display import display_current, display_forecast


def main():
    api = WeatherAPI()

    while True:
        print("\n=== WEATHER DASHBOARD ===")
        city = input("Enter city name (or 'exit'): ").strip()
        if city.lower() == "exit":
            break

        current = api.current_weather(city)
        forecast = api.forecast(city)

        if not current or not forecast:
            print("Unable to fetch weather data.")
            continue

        display_current(parse_current(current))
        display_forecast(parse_forecast(forecast))


if __name__ == "__main__":
    main()
