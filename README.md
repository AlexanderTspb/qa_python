# qa_python  
#### В данном проекте реализованы unit-тесты для проверки приложения BooksCollector:  
1. test_genres_of_book_exist - проверяет, что поле genre содержит список жанров  
2. test_genres_age_rating_of_book_exist - проверяет, что поле genre_age_rating содержит список жанров с возрастным рейтингом  
3. test_set_book_genre_when_genre_does_not_exist - проверяет установку жанра, который не входит в список genre  
4. test_add_new_book_when_book_name_is_incorrect - проверяет добавление книги с некорректными названиями  
5. test_set_book_genre_when_book_with_the_given_name_exist - проверяет установку жанра добавленной книге, жанр входит в список genre  
6. test_get_book_genre_when_book_with_given_name_exists - проверяет получение жанра добавленной книги, жанр входит в список genre  
7. test_get_books_with_specific_genre_when_books_with_given_genre_exist - проверяет получение списка книг с определённым жанром, жанр входит в список genre  
8. test_add_book_in_favorites_when_book_exists_and_is_not_in_favorites - проверяет добавление книги в список избранного, книга изначально не находится в списке избранного  
9. test_delete_book_from_favorites_when_book_exists_and_is_in_favorites - проверяет удаление книги из списка избранного, книга изначально находится в списке избранного  
10. test_get_books_for_children_when_such_books_exist - проверяет получение списка книг без жанров из списка с возрастным рейтингом  
11. test_get_books_genre_when_books_are_added - проверяет получение списка добавленных книг  
12. test_get_list_of_favorites_books_when_books_are_favorited - ппроверяет получение списка добавленных в избранное книг  