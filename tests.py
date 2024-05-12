import pytest
from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()
def test_add_new_book():
    collector = BooksCollector()
    collector.add_new_book("Гарри Поттер")
    assert "Гарри Поттер" in collector.get_books_genre()


def test_set_book_genre():
    collector = BooksCollector()
    collector.add_new_book("Страга севера")
    collector.set_book_genre("Страга севера", "Фантастика")
    assert collector.get_book_genre("Страга севера") == "Фантастика"


def test_get_book_genre():
    collector = BooksCollector()
    collector.add_new_book("Собака Баскервилей")
    collector.set_book_genre("Собака Баскервилей", "Детективы")
    assert collector.get_book_genre("Собака Баскервилей") == "Детективы"


def test_get_books_with_specific_genre():
    collector = BooksCollector()
    collector.add_new_book("Властелин Колец")
    collector.set_book_genre("Властелин Колец", "Фантастика")
    assert collector.get_books_with_specific_genre("Фантастика") == ["Властелин Колец"]


def test_get_books_genre():
    collector = BooksCollector()

    collector.add_new_book("Гарри Поттер")
    collector.set_book_genre("Гарри Поттер", "Фантастика")

    collector.add_new_book("Собака Баскервилей")
    collector.set_book_genre("Собака Баскервилей", "Детективы")

    expected_books_genre = {"Гарри Поттер": "Фантастика", "Собака Баскервилей": "Детективы"}
    assert collector.get_books_genre() == expected_books_genre


def test_get_books_for_children():
    collector = BooksCollector()
    collector.add_new_book("Колобок")
    collector.set_book_genre("Колобок", "Мультфильмы")
    assert "Колобок" in collector.get_books_for_children()


def test_add_book_in_favorites():
    collector = BooksCollector()
    collector.add_new_book("Собака Баскервилей")
    collector.add_book_in_favorites("Собака Баскервилей")
    assert "Собака Баскервилей" in collector.get_list_of_favorites_books()


def test_delete_book_from_favorites():
    collector = BooksCollector()
    collector.add_new_book("Собака Баскервилей")
    collector.add_book_in_favorites("Собака Баскервилей")
    collector.delete_book_from_favorites("Собака Баскервилей")
    assert "Собака Баскервилей" not in collector.get_list_of_favorites_books()


def test_get_list_of_favorites_books():
    collector = BooksCollector()
    collector.add_new_book("Собака Баскервилей")
    collector.add_book_in_favorites("Собака Баскервилей")
    assert collector.get_list_of_favorites_books() == ["Собака Баскервилей"]

if __name__ == "__main__":
    pytest.main()