from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from weather_adapter import WeatherAdapter
from auth_decorator import require_auth_basic

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="index.html"
    )


@app.get("/weather")
@require_auth_basic
async def get_weather(request: Request, city: str = ""):

    import os
    import random
    import hashlib

    api_key = os.getenv("OPENWEATHER_API_KEY")

    # Fallback demo data
    if not api_key:

        city_key = city.strip() if city else "Sample City"

        seed = int(
            hashlib.sha256(city_key.encode()).hexdigest(),
            16
        ) % (2 ** 32)

        rng = random.Random(seed)

        return {
            "city": city_key,
            "temperature": round(rng.uniform(20, 40), 1),
            "humidity": rng.randint(20, 70),
            "weather": rng.choice([
                "clear sky",
                "cloudy",
                "rain",
                "mist"
            ])
        }

    adapter = WeatherAdapter(api_key)

    return adapter.get_weather(city)