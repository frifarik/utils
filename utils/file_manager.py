import json
import os


def read_txt(filepath: str) -> list[str]:
    """Читает содержимое текстового файла и возвращает его как строку."""
    with open(os.path.abspath(filepath), 'r', encoding='utf-8') as file:
        return [line.strip() for line in file.readlines() if line != "\n"]


def write_txt(filepath: str, content: str) -> None:
    """Записывает строку в текстовый файл, сохраняя уже имеющиеся строки."""
    with open(os.path.abspath(filepath), 'a', encoding='utf-8') as file:
        file.write(f"\n{content}")


def rewrite_txt(filepath: str, content: str) -> None:
    """Перезаписывает содержимое текстового файла новым содержимым."""
    with open(os.path.abspath(filepath), 'w', encoding='utf-8') as file:
        file.write(content)


def read_json(filepath: str) -> dict:
    """Читает содержимое json файла и возвращает его как словарь."""
    with open(os.path.abspath(filepath), 'r', encoding='utf-8') as file:
        return json.load(file)


def write_json(filepath: str | str, data) -> None:
    """Записывает данные в json файл, сохраняя уже имеющиеся."""
    with open(os.path.abspath(filepath), 'r', encoding='utf-8') as file_read:
        unified_data = json.load(file_read)

    unified_data.update(data)

    with open(os.path.abspath(filepath), 'w', encoding='utf-8') as file_write:
        json.dump(unified_data, file_write, indent=4)


def rewrite_json(filepath: str | str, data) -> None:
    """Перезаписывает содержимое json файла новыми данными."""
    with open(os.path.abspath(filepath), 'w', encoding='utf-8') as file_write:
        json.dump(data, file_write, indent=4)