# 🌤️ Weather Dashboard Application

**Week 6 – Working with External Libraries**

---

## 📌 Project Overview

The **Weather Dashboard Application** is a command-line based Python project that fetches real-time weather data using an external weather API. The application demonstrates professional usage of **external libraries**, **API integration**, **JSON processing**, **environment variables**, and **modular code design**.

This project is part of **Week 6** and focuses on working with third-party APIs and libraries using best development practices.

---

## 🎯 Objectives

* Learn how to work with **external Python libraries**
* Understand **API requests and responses**
* Handle **JSON data** efficiently
* Use **environment variables** securely
* Implement **caching** to reduce API calls
* Build a clean, user-friendly command-line interface

---

## 🧠 Concepts Covered

* Package management using `pip`
* Virtual environments
* HTTP requests using `requests`
* JSON parsing and formatting
* Date & time handling
* API documentation understanding
* Environment variable management
* Error handling for network and API failures

---

## 🛠️ Features

* Fetch **current weather** for any city worldwide
* Display **5-day weather forecast**
* Shows:

  * Temperature
  * Humidity
  * Wind speed
  * Weather conditions
* API response **caching** (10 minutes)
* Error handling for:

  * Invalid city names
  * Network issues
  * API failures
* Clean and modular code structure
* User-friendly command-line interface

---

## 📂 Project Structure

```
week6-weather-dashboard/
│
├── weather_app/
│   ├── __init__.py
│   ├── config.py
│   ├── weather_api.py
│   ├── weather_parser.py
│   ├── weather_display.py
│   └── main.py
│
├── data/
│   ├── cache/
│   └── favorites.json
│
├── tests/
│   ├── test_api.py
│   ├── test_parser.py
│   └── test_display.py
│
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

---

## ⚙️ Technologies & Libraries Used

* **Python 3**
* **requests** – For HTTP API calls
* **python-dotenv** – For environment variable management
* **OpenWeatherMap API** – Weather data source

---

## 🚀 How to Run the Project

### Step 1: Get API Key

* Create a free account on **OpenWeatherMap**
* Generate an API key

### Step 2: Setup Environment

```bash
git clone <repository-url>
cd week6-weather-dashboard
```

### Step 3: Create `.env` File

```bash
cp .env.example .env
```

Add your API key:

```
WEATHER_API_KEY=your_api_key_here
```

### Step 4: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 5: Run Application

```bash
python -m weather_app.main
```

---

## 📊 Sample Output

```
=== WEATHER DASHBOARD ===
Enter city name: London

Current Weather
------------------------------
Location   : London, GB
Temperature: 8 °C
Condition  : light rain
Humidity   : 87%
Wind Speed : 22 km/h
Updated At : 2024-01-25 10:15:00

5-Day Forecast
------------------------------
2024-01-26: 6°C / 9°C - rain
2024-01-27: 4°C / 8°C - cloudy
2024-01-28: 3°C / 7°C - clear
```

---

## 🧪 Testing

Basic unit tests are included to verify:

* API module initialization
* Weather data parsing
* Display module execution

Run tests manually or using:

```bash
python -m unittest
```

---

## 🧾 What I Learned

* How to integrate **real-world APIs**
* Working with **external Python libraries**
* Managing **sensitive data using environment variables**
* Handling API errors gracefully
* Structuring medium-scale Python projects professionally
* Implementing caching for performance optimization

---

## ✅ Quality Standards Checklist

* ✔ Modular and clean code
* ✔ External API integration
* ✔ Error handling implemented
* ✔ Environment variables used securely
* ✔ Clear documentation
* ✔ Professional project structure
* ✔ Ready for GitHub and internship submission

---

## 👩‍💻 Author

**Mehak Tewari**
Week 6 – Python Training Program

---
