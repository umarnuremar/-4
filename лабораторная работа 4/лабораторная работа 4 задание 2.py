import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    try:
        with open(INPUT_FILENAME, 'r', newline='') as csvfile, \
                open(OUTPUT_FILENAME, 'w') as jsonfile:
            reader = csv.DictReader(csvfile)  # используем csvfile вместо "input.csv"
            data = list(reader)
            json.dump(data, jsonfile, indent=4)
    except FileNotFoundError:
        print(f"Ошибка: Файл '{INPUT_FILENAME}' не найден.")
    except Exception as e:
        print(f"Ошибка: {e}")


if __name__ == '__main__':
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
