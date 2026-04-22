import sys
from pathlib import Path
from typing import List, Dict, Optional


def parse_log_line(line: str) -> dict:
    """Парсить рядок логу у словник."""
    parts = line.split(maxsplit=3)
    if len(parts) < 4:
        return {}
    return {
        'date': parts[0],
        'time': parts[1],
        'level': parts[2].upper(),
        'message': parts[3].strip()
    }


def load_logs(file_path: str) -> List[dict]:
    """Завантажує логи з файлу, ігноруючи порожні або некоректні рядки."""
    path = Path(file_path)
    if not path.exists():
        print(f"Помилка: Файл '{file_path}' не знайдено.")
        sys.exit(1)

    logs = []
    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                parsed = parse_log_line(line)
                if parsed:
                    logs.append(parsed)
    except Exception as e:
        print(f"Помилка при читанні файлу: {e}")
        sys.exit(1)
    return logs


def filter_logs_by_level(logs: List[dict], level: str) -> List[dict]:
    """Фільтрує список логів за рівнем (використовуємо функціональний підхід)."""
    return list(filter(lambda x: x['level'] == level.upper(), logs))


def count_logs_by_level(logs: List[dict]) -> Dict[str, int]:
    """Підраховує кількість входжень кожного рівня логування."""
    counts = {}
    for entry in logs:
        level = entry['level']
        counts[level] = counts.get(level, 0) + 1
    return counts


def display_log_counts(counts: Dict[str, int]):
    """Виводить статистику у вигляді таблиці."""
    print(f"{'Рівень логування':<17} | {'Кількість':<10}")
    print("-" * 18 + "|" + "-" * 11)
    # Сортуємо для краси
    for level, count in sorted(counts.items(), key=lambda x: x[1], reverse=True):
        print(f"{level:<17} | {count:<10}")


def main():
    # Перевірка наявності аргументу шляху
    if len(sys.argv) < 2:
        print("Використання: python main.py /шлях/до/файлу.log [рівень]")
        return

    file_path = sys.argv[1]
    logs = load_logs(file_path)
    counts = count_logs_by_level(logs)

    # Виводимо загальну статистику
    display_log_counts(counts)

    # Якщо вказано рівень логування
    if len(sys.argv) > 2:
        level_to_filter = sys.argv[2].upper()
        filtered = filter_logs_by_level(logs, level_to_filter)

        if filtered:
            print(f"\nДеталі логів для рівня '{level_to_filter}':")
            for entry in filtered:
                print(f"{entry['date']} {entry['time']} - {entry['message']}")
        else:
            print(f"\nЗаписів для рівня '{level_to_filter}' не знайдено.")


if __name__ == "__main__":
    main()
