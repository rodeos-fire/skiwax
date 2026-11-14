# === Stage 1: Каркас модуля ===
# Project: SkiWax
from dataclasses import dataclass, field
from datetime import date


@dataclass
class Skis:
    model: str
    length: int
    stiffness: int
    sharpened_date: date


def make_demo_skis() -> list[Skis]:
    return [
        Skis(model="Rossignol Experience 88", length=185, stiffness=7, sharpened_date=date(2024, 3, 15)),
        Skis(model="Head Supershape 98", length=190, stiffness=6, sharpened_date=date(2024, 3, 20)),
        Skis(model="Fischer RC4 RC4 Worldcup", length=180, stiffness=9, sharpened_date=date(2024, 3, 10)),
    ]


def main() -> None:
    skis = make_demo_skis()
    print("SkiWax — доступные пары лыж:")
    for ski in skis:
        print(f"  {ski.model} | длина {ski.length} см | жёсткость {ski.stiffness} | заточка {ski.sharpened_date}")
    print(f"Всего пар: {len(skis)}")


if __name__ == "__main__":
    main()
