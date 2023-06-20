BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]


# TODO написать класс Book
class Book:
    def __init__(self, id_: int, name: str, pages: int):
        self.id = id_
        self.name = name
        self.pages = pages

    def __str__(self):
        return f'Книга "{self.name}", id={self.id}'

    def __repr__(self):
        return f'Book(id_={self.id}, name=\'{self.name}\', pages={self.pages})'


# TODO написать класс Library
class Library:
    def __init__(self, books=None):
        # Если список книг не передан, то инициализируем пустым списком
        self.books = books or []

    # Метод для получения id, который будет использоваться для добавления новой книги в библиотеку
    def get_next_book_id(self):
        if not self.books:
            # Если списка книг нет, то возвращаем 1
            return 1
        # Если список книг не пуст, то возвращаем идентификатор последней книги увеличенный на 1
        return self.books[-1].id + 1

    # Метод для получения индекса книги по её id
    def get_index_by_book_id(self, book_id):
        for i, book in enumerate(self.books):
            if book.id == book_id:
                # Если книга найдена, то возвращаем её индекс
                return i
        # Если книги с таким id нет в списке, то делаем исключение с сообщением об ошибке
        raise ValueError(f'Книги с запрашиваемым id={book_id} не существует')

if __name__ == '__main__':
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки

    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки

    print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1
