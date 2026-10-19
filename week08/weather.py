import argparse
import importlib
import os
import sys
from pathlib import Path

if __package__:
    from .favorites import FavoritesManager
    from .weather_api import WeatherAPI, format_current_weather, format_forecast
else:
    from favorites import FavoritesManager
    from weather_api import WeatherAPI, format_current_weather, format_forecast


FAVORITES_FILE = Path(__file__).with_name("favorites.json")


def load_api_key():
    api_key = os.environ.get("WEATHER_API_KEY")
    if api_key:
        return api_key

    config_module = f"{__package__}.config" if __package__ else "config"
    try:
        config = importlib.import_module(config_module)
    except ModuleNotFoundError as error:
        if error.name == config_module:
            return None
        raise
    return getattr(config, "WEATHER_API_KEY", None) or None


def build_parser():
    parser = argparse.ArgumentParser(description="Get weather and manage favorite locations.")
    commands = parser.add_subparsers(dest="command", required=True)

    current = commands.add_parser("current", help="Show current weather")
    current.add_argument("location")

    forecast = commands.add_parser("forecast", help="Show a weather forecast")
    forecast.add_argument("location")
    forecast.add_argument("--days", type=int, default=3)

    favorites = commands.add_parser("favorites", help="Manage favorite locations")
    favorite_commands = favorites.add_subparsers(
        dest="favorites_command", required=True
    )

    add = favorite_commands.add_parser("add", help="Add a favorite location")
    add.add_argument("name")
    add.add_argument("location")

    favorite_commands.add_parser("list", help="List favorite locations")

    remove = favorite_commands.add_parser("remove", help="Remove a favorite location")
    remove.add_argument("name")

    return parser


def main(argv=None) -> int:
    args = build_parser().parse_args(argv)
    manager = FavoritesManager(FAVORITES_FILE)

    if args.command == "favorites":
        if args.favorites_command == "add":
            if not manager.add(args.name, args.location):
                print(f"Favorite '{args.name}' already exists.", file=sys.stderr)
                return 1
            print(f"Added favorite '{args.name}'.")
            return 0

        if args.favorites_command == "list":
            for name, location in manager.list_all().items():
                print(f"{name}: {location}")
            return 0

        if not manager.remove(args.name):
            print(f"Favorite '{args.name}' does not exist.", file=sys.stderr)
            return 1
        print(f"Removed favorite '{args.name}'.")
        return 0

    api_key = load_api_key()
    if not api_key:
        print("Weather API key is missing.", file=sys.stderr)
        return 1

    location = manager.get_location(args.location) or args.location
    client = WeatherAPI(api_key)
    if args.command == "current":
        data = client.get_current_weather(location)
        formatter = format_current_weather
    else:
        try:
            data = client.get_forecast(location, days=args.days)
        except ValueError as error:
            print(str(error), file=sys.stderr)
            return 1
        formatter = format_forecast

    if data is None:
        print("Weather request failed.", file=sys.stderr)
        return 1

    print(formatter(data))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
