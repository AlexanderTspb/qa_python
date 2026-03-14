from main import BooksCollector
import pytest
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

    def test_genres_of_book_exist(self):
        collector = BooksCollector()   
        assert collector.genre == ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии']

    def test_genres_age_rating_of_book_exist(self):
        collector = BooksCollector()   
        assert collector.genre_age_rating == ['Ужасы', 'Детективы']
    
    def test_set_book_genre_when_genre_does_not_exist(self):
        collector = BooksCollector()
        collector.add_new_book('Норвежский лес')
        collector.set_book_genre('Норвежский лес', 'Роман')
        assert collector.books_genre.get('Норвежский лес') == ''

    @pytest.mark.parametrize('name', ['', 
                                      'Сказка о царе Салтане, о сыне его славном и могучем богатыре князе Гвидоне Салтановиче и о прекрасной царевне Лебеди', 
                                      'Тайны древних рун Ривенделла: сказание эльфов'])
    def test_add_new_book_when_book_name_is_incorrect(self, name):
        collector = BooksCollector()
        collector.add_new_book(name)
        assert len(collector.get_books_genre()) == 0

    @pytest.mark.parametrize(
        'name, genre',
        [
            ['«Хребты безумия', 'Ужасы'],
            ['Марсианин', 'Фантастика'],
            ['Волшебник Изумрудного города', 'Мультфильмы'],
            ['Понедельник начинается в субботу', 'Комедии'],
            ['Приключения Шерлока Холмса', 'Детективы'],
        ]
    )
    def test_set_book_genre_when_book_with_the_given_name_exist(self, name, genre):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert collector.books_genre.get(name) == genre

    @pytest.mark.parametrize(
        'name, genre',
        [
            ['«Хребты безумия', 'Ужасы'],
            ['Марсианин', 'Фантастика'],
            ['Волшебник Изумрудного города', 'Мультфильмы'],
            ['Понедельник начинается в субботу', 'Комедии'],
            ['Приключения Шерлока Холмса', 'Детективы'],
        ]
    )
    def test_get_book_genre_when_book_with_given_name_exists(self, name, genre):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert collector.get_book_genre(name) == genre

    @pytest.mark.parametrize(
        'books, genre, book_list',
        [
            [{'«Хребты безумия':'Ужасы', 'Властелин колец':'Фантастика', 'Дюна':'Фантастика', 'Мизери':'Ужасы' }, 'Ужасы', ['«Хребты безумия', 'Мизери']],
            [{'«Хребты безумия':'Ужасы', 'Горе от ума':'Комедия', 'Дюна':'Фантастика', 'Мизери':'Ужасы' }, 'Фантастика', ['Дюна']]
        ]
    )
    def test_get_books_with_specific_genre_when_books_with_given_genre_exist(self, books, genre, book_list):
        collector = BooksCollector()
        for name, book_genre in books.items():
            collector.add_new_book(name)
            collector.set_book_genre(name, book_genre)
        books_with_genre = collector.get_books_with_specific_genre(genre)
        assert books_with_genre == book_list

    def test_add_book_in_favorites_when_book_exists_and_is_not_in_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Властелин колец')
        collector.set_book_genre('Властелин колец', 'Фантастика')
        collector.add_book_in_favorites('Властелин колец')
        assert collector.get_list_of_favorites_books() == ['Властелин колец']

    def test_delete_book_from_favorites_when_book_exists_and_is_in_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Властелин колец')
        collector.set_book_genre('Властелин колец', 'Фантастика')
        collector.add_book_in_favorites('Властелин колец')
        collector.add_new_book('Ведьмак')
        collector.set_book_genre('Ведьмак', 'Фантастика')
        collector.add_book_in_favorites('Ведьмак')
        collector.delete_book_from_favorites('Властелин колец')
        assert collector.get_list_of_favorites_books() == ['Ведьмак']

    def test_get_books_for_children_when_such_books_exist(self):
        collector = BooksCollector()
        books = {'Властелин колец':'Фантастика', 'Мизери':'Ужасы', 'Волшебник Изумрудного города':'Мультфильмы', 'Приключения Шерлока Холмса':'Детективы' }
        for name, book_genre in books.items():
            collector.add_new_book(name)
            collector.set_book_genre(name, book_genre)
        assert collector.get_books_for_children() == ['Властелин колец', 'Волшебник Изумрудного города']
