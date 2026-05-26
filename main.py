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
def add_book(books):
    author = input("Автор: ")
    title = input("Название: ")

    # Проверка на дубликаты
    for book in books:
        if book['author'] == author and book['title'] == title:
            print("Эта книга уже есть в списке!")
            return

    while True:
        try:
            rating = int(input("Оценка (1–5): "))
            if 1 <= rating <= 5:
                break
            else:
                print("Оценка должна быть от 1 до 5.")
        except ValueError:
            print("Введите число от 1 до 5.")

    date = input("Дата прочтения (YYYY-MM-DD): ") or datetime.now().strftime('%Y-%m-%d')

    new_book = {
        'author': author,
        'title': title,
        'rating': rating,
        'date': date
    }
    books.append(new_book)
    save_books(books)
    print("Книга добавлена!")

def list_books(books):
    if not books:
        print("Список книг пуст.")
        return
    for i, book in enumerate(books, 1):
        print(f"{i}. {book['title']} — {book['author']} ({book['rating']}/5, {book['date']})")

def show_average_rating(books):
    if not books:
        print("Нет книг для расчёта средней оценки.")
        return
    avg = sum(book['rating'] for book in books) / len(books)
    print(f"Средняя оценка: {avg:.2f}")

def show_author_stats(books):
    from collections import defaultdict
    stats = defaultdict(int)
    for book in books:
        stats[book['author']] += 1
    print("Статистика по авторам:")
    for author, count in stats.items():
        print(f"{author}: {count} книг")
def delete_book(books):
    list_books(books)
    if not books:
        return
    try:
        index = int(input("Введите номер книги для удаления: ")) - 1
        if 0 <= index < len(books):
            removed = books.pop(index)
            save_books(books)
            print(f"Книга '{removed['title']}' удалена.")
        else:
            print("Неверный номер.")
    except ValueError:
        print("Введите корректный номер.")

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

