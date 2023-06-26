class Review:
    def __init__(self, rating, comment, date, username, review_id):
        """
        Создание объекта отзыва

        :param rating: рейтинг отзыва (от 1 до 5)
        :param comment: текст отзыва
        :param date: дата отзыва
        :param username: имя пользователя, оставившего отзыв
        :param review_id: идентификатор отзыва
        """
        self.rating = rating
        self.comment = comment
        self.date = date
        self.username = username
        # Пример расширения функционала: новый атрибут review_id
        # для идентификации конкретного отзыва
        self.review_id = review_id