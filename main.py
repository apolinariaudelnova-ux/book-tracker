import json
from datetime import datetime

def load_books():
    try:
        with open('books.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_books(books):
    with open('books.json', 'w', encoding='utf-8') as f:
        json.dump(books, f, ensure_ascii=False, indent=2)

def main():
    books = load_books()
    while True:
        print("\n1. Добавить книгу")
        print("2. Показать все книги")
        print("3. Показать среднюю оценку")
        print("4. Статистика по авторам")
        print("5. Удалить книгу")
        print("6. Выход")

        choice = input("Выберите действие: ")

        if choice == '1':
            add_book(books)
        elif choice == '2':
            list_books(books)
        elif choice == '3':
            show_average_rating(books)
        elif choice == '4':
            show_author_stats(books)
        elif choice == '5':
            delete_book(books)
        elif choice == '6':
            break
        else:
            print("Неверный выбор, попробуйте снова.")

if __name__ == "__main__":
    main()
