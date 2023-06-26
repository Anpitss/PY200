from review import Review

class ReviewStorage:
    def __init__(self):
        """
        Создание объекта хранилища отзывов
        """
        self.reviews = []

    def add_review(self, review):
        """
        Добавление отзыва в хранилище

        :param review: объект отзыва
        """
        self.reviews.append(review)

    def remove_review(self, review):
        """
        Удаление отзыва из хранилища

        :param review: объект отзыва
        """
        self.reviews.remove(review)

    def get_reviews(self):
        """
        Получение списка всех отзывов в хранилище

        :return: список объектов отзывов
        """
        return self.reviews

    # Пример расширения функционала: метод get_review_by_id
    # в класс ReviewStorage для получения отзыва по его review_id
    def get_review_by_id(self, review_id):
        """
        Получение отзыва по его идентификатору

        :param review_id: идентификатор отзыва
        :return: объект отзыва
        """
        for review in self.reviews:
            if review.review_id == review_id:
                return review