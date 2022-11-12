from rest_framework import serializers
from app_library.models import Book, Author


class AuthorSerializer(serializers.ModelSerializer):
    """
    Класс - сериалайзер для модели Автор
    """
    class Meta:
        model = Author
        fields = ['id', 'name', 'surname', 'date_of_birth']


class BookSerializer(serializers.ModelSerializer):
    """
    Класс - сериалайзер для модели Книга
    """
    # author_book = AuthorSerializer()

    class Meta:
        model = Book
        fields = ['id', 'title', 'isbn', 'year_of_release', 'number_of_pages', 'author_book']

