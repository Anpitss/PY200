import unittest

from review import Review
from review_storage import ReviewStorage
from review_analyzer import ReviewAnalyzer

class TestReviewAnalyzer(unittest.TestCase):
    # начальные значения для тестов
    def setUp(self):
        # два экземпляра класса Review
        self.review1 = Review(4, "Good product", "2020-01-01", "user1", 1)
        self.review2 = Review(2, "Bad product", "2020-01-02", "user2", 2)

        # экземпляр класса ReviewStorage и два экземпляра класса Review
        self.storage = ReviewStorage()
        self.storage.add_review(self.review1)
        self.storage.add_review(self.review2)

        # экземпляр класса ReviewAnalyzer и экземпляр класса ReviewStorage
        self.analyzer = ReviewAnalyzer(self.storage)

    def test_get_avg_rating(self):
        # проверка возврата методом get_avg_rating класса ReviewAnalyzer средней оценки
        self.assertEqual(self.analyzer.get_avg_rating(), 3.0)

    def test_get_review_count(self):
        # проверка возврата кол-ва отзывов методом get_review_count класса ReviewAnalyzer
        self.assertEqual(self.analyzer.get_review_count(), 2)

    def test_get_positive_review_count(self):
        # проверка возврата кол-ва положительных отзывов методом get_positive_review_count класса ReviewAnalyzer
        self.assertEqual(self.analyzer.get_positive_review_count(), 1)

    def test_get_negative_review_count(self):
        # проверка возврата кол-ва отрицательных отзывов методом get_negative_review_count класса ReviewAnalyzer
        self.assertEqual(self.analyzer.get_negative_review_count(), 1)

    def test_get_review_by_id(self):
        # проверка возврата отзыва по заданному идентификатору методом get_review_by_id класса ReviewStorage
        self.assertEqual(self.storage.get_review_by_id(1), self.review1)

if __name__ == '__main__':
    unittest.main()