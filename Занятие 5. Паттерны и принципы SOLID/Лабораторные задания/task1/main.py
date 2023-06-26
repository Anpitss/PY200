#  подсчет отзывов пользователей на сайте интернет-магазина
from review_storage import ReviewStorage
from review_analyzer import ReviewAnalyzer
from review import Review

if __name__ == "__main__":
    review1 = Review(4, "Good product", "2020-01-01", "user1", 1)
    review2 = Review(2, "Bad product", "2020-01-02", "user2", 2)

    storage = ReviewStorage()
    storage.add_review(review1)
    storage.add_review(review2)

    analyzer = ReviewAnalyzer(storage)

    print("Review with id 1:", storage.get_review_by_id(1))