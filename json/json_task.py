import json
from json import JSONDecodeError


def process_books(file_path: str) -> None:
    """A function for editing books information in JSON files."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            books = json.load(file)

        print("The list of available books:")

        available_books = [book for book in books if book.get('наявність') is True]

        if available_books:
            for book in available_books:
                print(f"The book {book['назва']} ({book['автор']})")
        else:
            print("Sadly no books available")

        new_book = {
            "назва": "Грокаємо алгоритми",
            "автор": "Адітья Бхаргава",
            "рік": 2016,
            "наявність": True
        }
        books.append(new_book)

        with open(file_path, "w", encoding="utf-8") as file:
            json.dump(books, file, indent=4, ensure_ascii=False)

        print(f"\n A book called '{new_book['назва']}' was successfully added")

    except FileNotFoundError:
        print("The file was not found")
    except JSONDecodeError:
        print("The file is invalid")


if __name__ == "__main__":
    process_books('books.json')