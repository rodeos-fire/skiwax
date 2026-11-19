# === Stage 3: Хранилище в памяти ===
# Project: SkiWax
storage_skis.py

from typing import Dict, List, Optional


class Ski:
    def __init__(self, model: str, length: int, stiffness: int, sharpened_date: str):
        self.model = model
        self.length = length
        self.stiffness = stiffness
        self.sharpened_date = sharpened_date

    def to_dict(self) -> Dict:
        return {
            "model": self.model,
            "length": self.length,
            "stiffness": self.stiffness,
            "sharpened_date": self.sharpened_date,
        }


class SkiStorage:
    def __init__(self):
        self._items: Dict[str, Ski] = {}

    def add(self, ski: Ski) -> None:
        self._items[ski.model] = ski

    def get(self, model: str) -> Optional[Ski]:
        return self._items.get(model)

    def list(self) -> List[Ski]:
        return list(self._items.values())


if __name__ == "__main__":
    storage = SkiStorage()

    ski1 = Ski("Atomic Redster X9", 185, 85, "2024-03-15")
    ski2 = Ski("Fischer RC3 WC", 190, 90, "2024-03-18")

    storage.add(ski1)
    storage.add(ski2)

    print("Добавлено лыж:", len(storage.list()))
    print("Лыжи:", storage.list())
    print("Получить Atomic Redster X9:", storage.get("Atomic Redster X9"))
    print("Получить несуществующую:", storage.get("NonExistent"))
