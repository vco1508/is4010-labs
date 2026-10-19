import json


class FavoritesManager:
    def __init__(self, filename):
        self.filename = filename
        self.favorites = self._load()

    def _load(self):
        try:
            with open(self.filename, "r", encoding="utf-8") as file:
                favorites = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return {}

        if not isinstance(favorites, dict):
            return {}
        return favorites

    def _save(self):
        with open(self.filename, "w", encoding="utf-8") as file:
            json.dump(self.favorites, file, indent=4)

    def add(self, name, location):
        key = name.casefold()
        if key in self.favorites:
            return False
        self.favorites[key] = location
        self._save()
        return True

    def remove(self, name):
        key = name.casefold()
        if key not in self.favorites:
            return False
        del self.favorites[key]
        self._save()
        return True

    def list_all(self):
        return self.favorites.copy()

    def get_location(self, name):
        return self.favorites.get(name.casefold())
