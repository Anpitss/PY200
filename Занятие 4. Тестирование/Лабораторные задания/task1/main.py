from abc import ABC


class Animal(ABC):
    def __init__(self, name: str, age: int, weight: float):
        self.name = name
        self.age = age
        self.weight = weight

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value: str):
        if not isinstance(value, str):
            raise TypeError("Имя должно быть записано в формате строки")
        self._name = value

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value: int):
        if not isinstance(value, int):
            raise TypeError("Возраст должен быть записан в формате целого числа")
        self._age = value

    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, value: float):
        if not isinstance(value, float):
            raise TypeError("Вес должен быть записан в формате числа с плавающей точкой")
        self._weight = value

    def sound(self):
        pass

    @staticmethod
    def static_method():
        return "static method"


class Dog(Animal):
    def __init__(self, name: str, age: int, weight: float, breed: str):
        super().__init__(name, age, weight)
        self.breed = breed

    @property
    def breed(self):
        return self._breed

    @breed.setter
    def breed(self, value: str):
        if not isinstance(value, str):
            raise TypeError("Порода должна быть записана в формате строки")
        self._breed = value

    def sound(self):
        return "Woof!"

    @classmethod
    def class_method(cls):
        return f"This is a {cls.__name__}"


class Cat(Animal):
    def __init__(self, name: str, age: int, weight: float, color: str):
        super().__init__(name, age, weight)
        self.color = color

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, value: str):
        if not isinstance(value, str):
            raise TypeError("Окрас должен быть записан в формате строки")
        self._color = value

    def sound(self):
        return "Meow!"

    def special_method(self):
        return f"{self.name} this is {self.color} cat"

if __name__ == "__main__":
    dog = Dog("Rex", 3, 20.0, "German Shepherd")
    cat = Cat("Kitty", 2, 5.0, "Multicolor")
    print(dog.sound())
    print(cat.special_method())
    print(Dog.static_method())