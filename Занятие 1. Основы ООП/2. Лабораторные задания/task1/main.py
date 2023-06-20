# TODO Написать 3 класса с документацией и аннотацией типов
import doctest
from typing import List, Union
class GeometricShape:
    """
    Класс, описывающий геометрическую фигуру
    """
    def __init__(self, sides: Union[int, float]):
        """
        Создаем геометрическую фигуру
        :param sides: Количество сторон фигуры
        """
        self.sides = self.validate_value(sides)

    def validate_value(self, value) -> int:
        """
        Проверка входных данных на корректность
        """
        if not isinstance(value, (int, float)):
            raise TypeError(f"Значение должно быть (int, float), а не {type(value)}")
        if value < 3:
            raise ValueError(f"Значение должно быть больше или равно 3")
        if not isinstance(value, int):
            raise TypeError("Количество сторон должно быть целым числом")
        return value

    def calculate_perimeter(self, side_length: Union[int, float]) -> float:
        """
        Вычисление периметра геометрической фигуры

        >>> shape = GeometricShape(4)
        >>> shape.calculate_perimeter(5)
        20

        """
        return self.sides * side_length

    def calculate_area(self, apothem_length: Union[int, float], side_length: Union[int, float]) -> float:
        """
        Вычисление площади геометрической фигуры
        """
        return 0.5 * self.sides * apothem_length * side_length

class Book:
    """
    Класс, представляющий книгу
    >>> book = Book('The Great Gatsby', 'F. Scott Fitzgerald', '9780521578611', 180, ['fiction', 'classic'])
    >>> book.get_book_info()
    'Название: The Great Gatsby\\nАвтор: F. Scott Fitzgerald\\nISBN: 9780521578611\\nКоличество страниц: 180\\nЖанры: fiction, classic\\n'
    """
    def __init__(self, title: str, author: str, isbn: Union[str, int], page_count: Union[int, float], genres: List[str]):
        """
        Создание книги с заданными свойствами
        :param title: название книги
        :param author: автор книги
        :param isbn: ISBN книги
        :param page_count: количество страниц в книге
        :param genres: жанры книги
        """
        self.title = title
        self.author = author
        self.isbn = self.validate_isbn(isbn)
        self.page_count = self.validate_page_count(page_count)
        self.genres = genres

    def validate_isbn(self, isbn: Union[str, int]) -> str:
        """
        Проверка ISBN книги на корректность
        >>> book = Book('The Great Gatsby', 'F. Scott Fitzgerald', '9780521578611', 180, ['fiction', 'classic'])
        >>> book.validate_isbn('9780521578611')
        '9780521578611'
        """
        if not isinstance(isbn, (str, int)):
            raise TypeError(f"ISBN должен быть (str, int), а не {type(isbn)}")
        if isinstance(isbn, int):
            isbn = str(isbn)
        if not isbn.isdigit() or len(isbn) != 13:
            raise ValueError("ISBN должен быть числом из 13 цифр")
        return isbn

    def validate_page_count(self, page_count: Union[int, float]) -> int:
        """
        Проверка количества страниц в книге на корректность
        >>> book = Book('The Great Gatsby', 'F. Scott Fitzgerald', '9780521578611', 180, ['fiction', 'classic'])
        >>> book.validate_page_count(180)
        180
        """
        if not isinstance(page_count, (int, float)):
            raise TypeError(f"Количество страниц должно быть (int, float), а не {type(page_count)}")
        if not isinstance(page_count, int):
            page_count = int(page_count)
        if page_count <= 0:
            raise ValueError("Количество страниц должно быть больше нуля")
        return page_count

    def get_book_info(self) -> str:
        """
        Получение информации о книге в виде строки
        >>> book = Book('The Great Gatsby', 'F. Scott Fitzgerald', '9780521578611', 180, ['fiction', 'classic'])
        >>> book.get_book_info()
        'Название: The Great Gatsby\\nАвтор: F. Scott Fitzgerald\\nISBN: 9780521578611\\nКоличество страниц: 180\\nЖанры: fiction, classic\\n'
        """
        info = f"Название: {self.title}\n"
        info += f"Автор: {self.author}\n"
        info += f"ISBN: {self.isbn}\n"
        info += f"Количество страниц: {self.page_count}\n"
        info += f"Жанры: {', '.join(self.genres)}\n"
        return info
class Pencil:
    """
    Класс, представляющий карандаш
    >>> pencil1 = Pencil('HB', 'Staedtler', 'black')
    >>> pencil1.get_pencil_info()
    'Тип карандаша: HB\\nПроизводитель: Staedtler\\nЦвет чернил: black\\n'
    """
    def __init__(self, pencil_type: str, manufacturer: str, ink_color: str):
        """
        Создание карандаша с заданными свойствами
        :param pencil_type: тип карандаша
        :param manufacturer: производитель карандаша
        :param ink_color: цвет чернил карандаша
        """
        self.pencil_type = pencil_type
        self.manufacturer = manufacturer
        self.ink_color = ink_color

    def get_pencil_info(self) -> str:
        """
        Получение информации о карандаше в виде строки
        >>> pencil1 = Pencil('HB', 'Staedtler', 'black')
        >>> pencil1.get_pencil_info()
        'Тип карандаша: HB\\nПроизводитель: Staedtler\\nЦвет чернил: black\\n'
        """
        info = f"Тип карандаша: {self.pencil_type}\n"
        info += f"Производитель: {self.manufacturer}\n"
        info += f"Цвет чернил: {self.ink_color}\n"
        return info

if __name__ == "__main__":
    doctest.testmod()