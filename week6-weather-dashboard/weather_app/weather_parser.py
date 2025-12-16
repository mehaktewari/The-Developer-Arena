from datetime import datetime


def parse_current(data):
    return {
        "city": data["name"],
        "country": data["sys"]["country"],
        "temp": data["main"]["temp"],
        "humidity": data["main"]["humidity"],
        "wind": data["wind"]["speed"],
        "condition": data["weather"][0]["description"],
        "updated": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }


def parse_forecast(data):
    forecast = {}
    for item in data["list"]:
        date = item["dt_txt"].split()[0]
        if date not in forecast:
            forecast[date] = {
                "min": item["main"]["temp_min"],
                "max": item["main"]["temp_max"],
                "condition": item["weather"][0]["description"]
            }
    return forecast
