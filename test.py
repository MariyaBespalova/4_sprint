from main import BooksCollector

class TestBooksCollector:

    def test_books_genre_true(books_collector):
        books_collector.books_genre = {}
        assert books_collector.book_genre == {}
 
    def test_favorites_true(books_collector):
        books_collector.favorites = []
        assert books_collector.favorites == []
    
    def test_genre_true(books_collector):
        books_collector.genre = ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии']
        assert books_collector.genre == ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии']
 
    def test_genre_age_rating_true(books_collector):
        books_collector.genre_age_rating = ['Ужасы', 'Детективы']
        assert books_collector.genre_age_rating == ['Ужасы', 'Детективы']
    
    def test_add_new_book_tittle_length_pozitive(books_collector):  # проверяем количество символов в названии книги
        valid_name = "Евгений Онегин"
        books_collector.add_new_book(valid_name)
        assert valid_name in books_collector.get_books_genre

    @pytest.mark.parametrize('name', ['Ф', 'Евгений ОнегинЕвгений ОнегинЕвгений ОнегинЕвгений ОнегинЕвгений Онегин'])
    def test_add_new_book_tittle_length_negative(books_collector, name):  # проверяем количество символов в названии книги
        books_collector.add_new_book(name)
        assert name not in books_collector.get_books_genre
 
    def test_add_new_book_name(books_collector):
        book_name = "Война и мир"
        books_collector.add_new_book(book_name)
        assert book_name in books_collector.books_genre
        books_collector.add_new_book(book_name)
        books_count = len(books_collector.books_genre)
        assert books_count == 1
 
    def test_set_book_genre_true(books_collector):
        name = 'Что делать, если ваш кот хочет вас убить'
        genre = 'Ужасы'
        books_collector.add_new_book(name)
        books_collector.set_book_genre(name, genre)
        assert books_collector.books_genre[name] == genre

    def test_get_book_genre(books_collector):
        name = 'Что делать, если ваш кот хочет вас убить'
        genre = 'Ужасы'
        books_collector.add_new_book(name)
        books_collector.set_book_genre(name, genre)
        assert books_collector.get_book_genre(name) == genre
 
    @pytest.mark.parametrize('name, genre', [['Книга 1', 'Ужасы'], ['Книга 2', 'Ужасы'],['Книга 3', 'Мультфильмы']])
    def test_get_books_with_specific_genre(books_collector, name, genre):
        books_collector.add_new_book(name)
        books_collector.set_book_genre(name, genre)
        scary_books = books_collector.get_books_with_specific_genre('Ужасы')
        assert 'Книга 1' in scary_books
        assert 'Книга 2' in scary_books
        assert len(scary_books) == 2
 
    def test_get_books_genre(books_collector, name, genre):
        books = [['Книга 1', 'Ужасы'], ['Книга 2', 'Ужасы'],['Книга 3', 'Мультфильмы']]
        for name, genre in books:
            books_collector.add_new_book(name)
            books_collector.set_book_genre(name, genre)
        result = books_collector.get_books_genre()
        expected_result = {'Книга 1': 'Ужасы', 'Книга 2': 'Ужасы', 'Книга 3': 'Мультфильмы'}
        assert result == expected_result

    def test_get_books_for_children(books_collector):
        books_collector.books_genre = {'Книга 1': 'Ужасы', 'Книга 2': 'Ужасы', 'Книга 3':'Мультфильмы'}
        books_collector.genre = ['Ужасы', 'Мультфильмы']
        books_collector.genre_age_rating = ['Ужасы']
        result = books_collector.get_books_for_children()
        expected_result = ['Книга 1', 'Книга 2']
        assert result == expected_result
 
    @pytest.mark.parametrize('book_name', ['Книга 1', 'Книга 2', 'Книга 3'])
    def test_add_book_in_favorites(books_collector, book_name):
        books_collector.add_new_book(book_name)
        books_collector.add_book_in_favorites(book_name)
        assert book_name in books_collector.favorites()
 
    @pytest.mark.parametrize('book_name', ['Книга 1', 'Книга 2', 'Книга 3'])
    def test_delete_book_from_favorites(books_collector, book_name):
        books_collector.add_new_book(book_name)
        books_collector.add_book_in_favorites(book_name)
        books_collector.delete_book_from_favorites(book_name)
        assert not book_name in books_collector.get_list_of_favorites_books()

    def test_get_list_of_favorites_books(books_collector):
        book_name = ['Книга 1', 'Книга 2', 'Книга 3']
        for book in book_name:
            books_collector.add_new_book(book)
            books_collector.add_book_in_favorites(book)
        for book in book_name:
            assert book in books_collector.favorites()