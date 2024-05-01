from pathlib import Path
import shutil
import argparse

"""
Напишіть програму на Python, яка рекурсивно копіює файли у вихідній директорії,
переміщає їх до нової директорії та сортує в піддиректорії, назви яких базуються на розширенні файлів.

Парсинг аргументів. Скрипт має приймати два аргументи командного рядка:
шлях до вихідної директорії та шлях до директорії призначення
(за замовчуванням, якщо тека призначення не була передана, вона повинна бути з назвою dist).
"""


def copy_and_sort_files(source_dir, dest_dir='dist'):
    try:
        source_path = Path(source_dir)
        dest_path = Path(dest_dir)

        dest_path.mkdir(parents=True, exist_ok=True)

        for file in source_path.iterdir():
            if file.is_file():
                extension = file.suffix

                extension_dir = dest_path / extension[1:]
                extension_dir.mkdir(parents=True, exist_ok=True)

                shutil.copy(file, extension_dir)

            elif file.is_dir():
                copy_and_sort_files(file, dest_path)

    except Exception as e:
        print(f"An error occurred: {e}")


parser = argparse.ArgumentParser(description='Copy and sort files recursively.')
parser.add_argument('source_dir', help='Path to the source directory')
parser.add_argument('dest_dir', nargs='?', default='dist', help='Path to the destination directory')
args = parser.parse_args()

copy_and_sort_files(args.source_dir, args.dest_dir)
