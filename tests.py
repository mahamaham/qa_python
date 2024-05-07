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
        assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    def setUp(self):
        self.bc = BooksCollector()

    def test_add_new_book(self):
        # Проверка добавления новой книги
        self.bc.add_new_book("Harry Potter")
        self.assertIn("Harry Potter", self.bc.get_books_genre())

        # Проверка на добавление одинаковой книги
        self.bc.add_new_book("Harry Potter")
        self.assertEqual(len(self.bc.get_books_genre()), 1)

        # Проверка добавления книги без указания жанра
        self.assertEqual(self.bc.get_book_genre("Harry Potter"), "")

    def test_set_book_genre(self):
        # Устанавливаем жанр для книги
        self.bc.add_new_book("Harry Potter")
        self.bc.set_book_genre("Harry Potter", "Фантастика")
        self.assertEqual(self.bc.get_book_genre("Harry Potter"), "Фантастика")

    def test_get_book_genre(self):
        # Получаем жанр книги
        self.bc.add_new_book("Harry Potter")
        self.bc.set_book_genre("Harry Potter", "Фантастика")
        self.assertEqual(self.bc.get_book_genre("Harry Potter"), "Фантастика")

    def test_get_books_with_specific_genre(self):
        # Получаем книги с определенным жанром
        self.bc.add_new_book("Harry Potter")
        self.bc.set_book_genre("Harry Potter", "Фантастика")
        self.bc.add_new_book("Sherlock Holmes")
        self.bc.set_book_genre("Sherlock Holmes", "Детективы")
        self.assertEqual(self.bc.get_books_with_specific_genre("Фантастика"), ["Harry Potter"])

    def test_get_books_genre(self):
        # Получаем словарь книг
        self.bc.add_new_book("Harry Potter")
        self.bc.set_book_genre("Harry Potter", "Фантастика")
        self.assertEqual(self.bc.get_books_genre(), {"Harry Potter": "Фантастика"})

    def test_get_books_for_children(self):
        # Получаем книги для детей
        self.bc.add_new_book("Frozen")
        self.bc.set_book_genre("Frozen", "Мультфильмы")
        self.bc.add_new_book("It")
        self.bc.set_book_genre("It", "Ужасы")
        children_books = self.bc.get_books_for_children()
        self.assertIn("Frozen", children_books)
        self.assertNotIn("It", children_books)

    def test_add_book_in_favorites(self):
        # Добавляем книгу в избранное
        self.bc.add_new_book("Harry Potter")
        self.bc.add_book_in_favorites("Harry Potter")
        self.assertIn("Harry Potter", self.bc.get_list_of_favorites_books())

    def test_delete_book_from_favorites(self):
        # Удаляем книгу из избранного
        self.bc.add_new_book("Harry Potter")
        self.bc.add_book_in_favorites("Harry Potter")
        self.bc.delete_book_from_favorites("Harry Potter")
        self.assertNotIn("Harry Potter", self.bc.get_list_of_favorites_books())

    def test_get_list_of_favorites_books(self):
        # Получаем список избранных книг
        self.bc.add_new_book("Harry Potter")
        self.bc.add_book_in_favorites("Harry Potter")
        self.assertEqual(self.bc.get_list_of_favorites_books(), ["Harry Potter"])