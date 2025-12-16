import requests
import json
import time
from pathlib import Path
from typing import Optional, Dict
from .config import API_KEY, BASE_URL, CACHE_DURATION


class WeatherAPI:
    def __init__(self):
        self.cache_dir = Path("data/cache")
        self.cache_dir.mkdir(parents=True, exist_ok=True)

    def _cache_path(self, key: str):
        return self.cache_dir / f"{key}.json"

    def _load_cache(self, key: str) -> Optional[Dict]:
        path = self._cache_path(key)
        if path.exists() and time.time() - path.stat().st_mtime < CACHE_DURATION:
            with open(path, "r") as f:
                return json.load(f)
        return None

    def _save_cache(self, key: str, data: Dict):
        with open(self._cache_path(key), "w") as f:
            json.dump(data, f, indent=2)

    def _request(self, endpoint: str, params: Dict) -> Optional[Dict]:
        params.update({"appid": API_KEY, "units": "metric"})
        try:
            res = requests.get(f"{BASE_URL}/{endpoint}", params=params, timeout=10)
            if res.status_code == 200:
                return res.json()
            print("API Error:", res.status_code)
        except requests.RequestException as e:
            print("Network Error:", e)
        return None

    def current_weather(self, city: str) -> Optional[Dict]:
        key = f"current_{city.lower()}"
        cached = self._load_cache(key)
        if cached:
            return cached

        data = self._request("weather", {"q": city})
        if data:
            self._save_cache(key, data)
        return data

    def forecast(self, city: str) -> Optional[Dict]:
        key = f"forecast_{city.lower()}"
        cached = self._load_cache(key)
        if cached:
            return cached

        data = self._request("forecast", {"q": city})
        if data:
            self._save_cache(key, data)
        return data
