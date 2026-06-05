import requests

class WeatherAdapter:

    def __init__(self, api_key):
        self.api_key = api_key

    def get_weather(self, city):

        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={self.api_key}&units=metric"

        response = requests.get(url)

        data = response.json()

        if response.status_code != 200:
            return {
                "error": data.get("message", "Unable to fetch weather")
            }

        # Adapt external API format into custom format
        return {
            "city": data["name"],
            "temperature": data["main"]["temp"],
            "humidity": data["main"]["humidity"],
            "weather": data["weather"][0]["description"]
        }