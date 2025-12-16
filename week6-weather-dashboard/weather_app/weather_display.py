def display_current(info):
    print("\nCurrent Weather")
    print("-" * 30)
    print(f"Location   : {info['city']}, {info['country']}")
    print(f"Temperature: {info['temp']} °C")
    print(f"Condition  : {info['condition']}")
    print(f"Humidity   : {info['humidity']}%")
    print(f"Wind Speed : {info['wind']} km/h")
    print(f"Updated At : {info['updated']}")


def display_forecast(forecast):
    print("\n5-Day Forecast")
    print("-" * 30)
    for date, info in forecast.items():
        print(f"{date}: {info['min']}°C / {info['max']}°C - {info['condition']}")
