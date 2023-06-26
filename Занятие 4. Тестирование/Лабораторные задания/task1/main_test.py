import unittest
from main import Animal, Dog, Cat


class TestAnimal(unittest.TestCase):
    def test_name(self):
        animal = Animal("Jo", 5, 10.0)
        self.assertEqual(animal.name, "Jo")

        with self.assertRaises(TypeError):
            animal.name = 123

    def test_age(self):
        animal = Animal("Jo", 5, 10.0)
        self.assertEqual(animal.age, 5)

        with self.assertRaises(TypeError):
            animal.age = "5"

    def test_weight(self):
        animal = Animal("Jo", 5, 10.0)
        self.assertEqual(animal.weight, 10.0)

        with self.assertRaises(TypeError):
            animal.weight = "10"

    def test_sound(self):
        animal = Animal("Jo", 5, 10.0)
        self.assertIsNone(animal.sound())


class TestDog(unittest.TestCase):
    def test_breed(self):
        dog = Dog("Rex", 3, 20.0, "German Shepherd")
        self.assertEqual(dog.breed, "German Shepherd")

        with self.assertRaises(TypeError):
            dog.breed = 123

    def test_sound(self):
        dog = Dog("Rex", 3, 20.0, "German Shepherd")
        self.assertEqual(dog.sound(), "Woof!")

    def test_class_method(self):
        self.assertEqual(Dog.class_method(), "This is a Dog")


class TestCat(unittest.TestCase):
    def test_color(self):
        cat = Cat("Kitty", 2, 5.0, "Multicolor")
        self.assertEqual(cat.color, "Multicolor")

        with self.assertRaises(TypeError):
            cat.color = 123

    def test_sound(self):
        cat = Cat("Kitty", 2, 5.0, "Multicolor")
        self.assertEqual(cat.sound(), "Meow!")

    def test_special_method(self):
        cat = Cat("Kitty", 2, 5.0, "Multicolor")
        self.assertEqual(cat.special_method(), "Kitty is a Multicolor cat")


if __name__ == "__main__":
    unittest.main()