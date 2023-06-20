class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    @property
    def name(self):
        return self._name

    @property
    def author(self):
        return self._author

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self._pages = pages

    @property
    def pages(self) -> int:
        return self._pages

    @pages.setter
    def pages(self, value):
        if not isinstance(value, int):
            raise TypeError("Количество страниц должно быть целым числом")
        if value < 1:
            raise ValueError("Количество страниц должно быть положительным числом")
        self._pages = value

    def __str__(self):
        return f"Бумажная {super().__str__()}. Количество страниц: {self.pages}"


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self._duration = duration

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, value):
        if not isinstance(value, (float, int)) or value <= 0:
            raise ValueError("Длительность должна быть числом больше 0")
        self._duration = value

    def __str__(self):
        return f"Аудио {super().__str__()}. Продолжительность: {self.duration} часов"


if __name__ == "__main__":
    book = Book('Анна Каренина', 'Л.Н. Толстой')
    p_book = PaperBook('Мартин Иден', 'Джек Лондон', 150)
    a_book = AudioBook('The Great Gatsby', 'Fitzgeralt', 40.3)
    print(book, p_book, a_book, sep='\n')
    print(a_book)


