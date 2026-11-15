# === Stage 2: Проверка полей ===
# Project: SkiWax
"""Модуль SkiWax: валидация сущности 'лыжи' и нормализация ввода."""

from datetime import datetime


class SkisValidationError(ValueError):
    """Исключение для некорректных данных сущности 'лыжи'."""


def normalize_text(value):
    """Убирает лишние пробелы и приводит текст к нижнему регистру."""
    if value is None:
        return ""
    return str(value).strip().lower()


def normalize_model(value):
    """Нормализует название модели лыж."""
    return normalize_text(value)


def normalize_length(value):
    """Приводит длину к числу с одним десятичным знаком."""
    cleaned = str(value).replace(",", ".").strip()
    return float(cleaned)


def normalize_stiffness(value):
    """Приводит жёсткость к целому числу."""
    cleaned = str(value).replace(",", ".").strip()
    return int(float(cleaned))


def normalize_sharpen_date(value):
    """Преобразует дату заточки в объект datetime."""
    formats = ("%Y-%m-%d", "%d.%m.%Y", "%d/%m/%Y")
    cleaned = str(value).strip()
    for fmt in formats:
        try:
            return datetime.strptime(cleaned, fmt)
        except ValueError:
            continue
    raise SkisValidationError("Дата заточки имеет неверный формат. Ожидаем DD.MM.YYYY или YYYY-MM-DD.")


def validate_skis(data):
    """Проверяет данные сущности 'лыжи' и возвращает нормализованный объект."""
    if not data:
        raise SkisValidationError("Данные лыж пусты.")

    model = normalize_model(data.get("model"))
    if not model:
        raise SkisValidationError("Модель лыж обязательна для заполнения.")

    length = normalize_length(data.get("length"))
    if length <= 0:
        raise SkisValidationError("Длина лыж должна быть больше нуля.")

    stiffness = normalize_stiffness(data.get("stiffness"))
    if stiffness <= 0:
        raise SkisValidationError("Жёсткость лыж должна быть больше нуля.")

    sharpen_date = normalize_sharpen_date(data.get("sharpen_date"))

    return {
        "model": model,
        "length": length,
        "stiffness": stiffness,
        "sharpen_date": sharpen_date,
    }
