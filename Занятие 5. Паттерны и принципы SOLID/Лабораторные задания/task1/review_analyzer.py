from review_storage import ReviewStorage

class ReviewAnalyzer:
    def __init__(self, storage):
        """
        Создание объекта анализатора отзывов

        :param storage: объект хранилища отзывов
        """
        self.storage = storage

    def get_avg_rating(self):
        """
        Получение среднего рейтинга всех отзывов

        :return: средний рейтинг
        """
        if len(self.storage.get_reviews()) == 0:
            return 0
        total = sum(review.rating for review in self.storage.get_reviews())
        return total / len(self.storage.get_reviews())

    def get_review_count(self):
        """
        Получение кол-ва отзывов в хранилище

        :return: кол-во отзывов
        """
        return len(self.storage.get_reviews())

    def get_positive_review_count(self):
        """
        Получение кол-ва положительных отзывов (рейтинг выше 3)

        :return: кол-во положительных отзывов
        """
        return len([review for review in self.storage.get_reviews() if review.rating > 3])

    def get_negative_review_count(self):
        """
        Получение кол-ва отрицательных отзывов (рейтинг ниже 3)

        :return: кол-во отрицательных отзывов
        """
        return len([review for review in self.storage.get_reviews() if review.rating < 3])