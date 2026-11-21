# === Stage 4: Редактирование записей ===
# Project: SkiWax
from datetime import date

ALLOWED_SKI_FIELDS = ("model", "length", "stiffness", "sharpening_date")


def update_ski(ski_id, changes):
    skis = _load_skis()
    if ski_id not in skis:
        return None, "Лыжи с таким id не найдены"

    ski = skis[ski_id]
    unknown = set(changes) - set(ALLOWED_SKI_FIELDS)
    if unknown:
        return None, f"Запрещённые поля: {', '.join(sorted(unknown))}"

    for field in ALLOWED_SKI_FIELDS:
        if field in changes:
            ski[field] = changes[field]

    _save_skis(skis)
    return ski, None


def _load_skis():
    try:
        with open("skis.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}


def _save_skis(skis):
    with open("skis.json", "w", encoding="utf-8") as f:
        json.dump(skis, f, indent=2, ensure_ascii=False)


if __name__ == "__main__":
    import json

    result, error = update_ski(1, {"length": 185, "stiffness": "medium"})
    if error:
        print(error)
    else:
        print(result)
