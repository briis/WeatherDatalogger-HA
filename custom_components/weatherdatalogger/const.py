"""Constants for the WeatherDataLogger integration."""

DOMAIN = "weatherdatalogger"
MANUFACTURER = "WeatherDatalogger"

CONF_LOCATION = "location"
CONF_PROVIDER = "provider"

DEFAULT_PORT = 3306
DEFAULT_DATABASE = "weatherdatalogger"
DEFAULT_LOCATION = "home"
DEFAULT_PROVIDER = "visualcrossing"

# Display name and attribution per forecast provider slug (the `provider`
# column / CONF_PROVIDER). An unknown slug falls back to the slug itself.
PROVIDER_NAMES = {
    "visualcrossing": "Visual Crossing",
    "openmeteo": "Open-Meteo",
}
# Open-Meteo's data is CC BY 4.0 and asks for this exact credit.
PROVIDER_ATTRIBUTIONS = {
    "visualcrossing": "Weather data provided by Visual Crossing",
    "openmeteo": "Weather data by Open-Meteo.com",
}


def provider_name(provider: str) -> str:
    """Human-readable name of a forecast provider slug."""
    return PROVIDER_NAMES.get(provider, provider)


def provider_attribution(provider: str) -> str:
    """Attribution text shown on the weather entity for a provider slug."""
    return PROVIDER_ATTRIBUTIONS.get(
        provider, f"Weather data provided by {provider_name(provider)}"
    )


DEFAULT_SCAN_INTERVAL = 60
MIN_SCAN_INTERVAL = 15
MAX_SCAN_INTERVAL = 300

WEATHER_DEVICE_NAME = "WeatherDataLogger Forecast"
STATION_DEVICE_NAME = "WeatherDataLogger Station"
