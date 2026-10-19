import requests


class WeatherAPI:
    def __init__(self, api_key, base_url="https://api.weatherapi.com/v1"):
        self.api_key = api_key
        self.base_url = base_url.rstrip("/")

    def get_current_weather(self, location):
        return self._get_data(
            f"{self.base_url}/current.json",
            {"key": self.api_key, "q": location},
        )

    def get_forecast(self, location, days=3):
        if isinstance(days, bool) or not isinstance(days, int) or not 1 <= days <= 3:
            raise ValueError("days must be between 1 and 3")
        return self._get_data(
            f"{self.base_url}/forecast.json",
            {"key": self.api_key, "q": location, "days": days},
        )

    @staticmethod
    def _get_data(url, params):
        try:
            response = requests.get(url, params=params, timeout=10)
            response.raise_for_status()
            return response.json()
        except (requests.exceptions.RequestException, ValueError):
            return None


def format_current_weather(data):
    location = data["location"]
    current = data["current"]
    condition = current["condition"]["text"]
    return (
        f'{location["name"]}, {location["country"]}: '
        f'{current["temp_f"]}°F, {condition}'
    )


def format_forecast(data):
    forecast_days = data["forecast"]["forecastday"]
    return "\n".join(
        f'{day["date"]}: high {day["day"]["maxtemp_f"]}°F, '
        f'low {day["day"]["mintemp_f"]}°F, {day["day"]["condition"]["text"]}'
        for day in forecast_days
    )
