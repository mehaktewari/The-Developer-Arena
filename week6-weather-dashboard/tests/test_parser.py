from weather_app.weather_parser import parse_current

def test_parse_current():
    sample = {
        "name": "TestCity",
        "sys": {"country": "TC"},
        "main": {"temp": 25, "humidity": 50},
        "wind": {"speed": 10},
        "weather": [{"description": "clear sky"}]
    }
    result = parse_current(sample)
    assert result["city"] == "TestCity"
