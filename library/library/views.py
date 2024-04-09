from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from .models import Author, Book

import json


class AuthorsAPI(APIView):

    def initial(self, request, *args, **kwargs):
        permission_classes = [AllowAny]

    def post(self, request):
        author = Author(name=request.data['name'],
                        gender=request.data['gender'])
        author.save()

        if request.data['books']:
            for book_id in json.loads(request.data['books']):
                book = Book.objects.get(id=book_id)
                author.books.add(book)

        return Response({'POST': 'Authors: Hello World!'}, 200)

    def patch(self, request):
        author = Author.objects.get(id=request.query_params['id'])
        if 'name' in request.data:
            author.name = request.data['name']

        if 'gender' in request.data:
            author.gender = request.data['gender']

        if 'books' in request.data:
            books = list()
            for book_id in json.loads(request.data['books']):
                books.append(Book.objects.get(id=book_id))
            author.books.set(books)

        author.save()

        return Response({'PATCH': 'Authors: Hello World!'}, 200)


class BooksAPI(APIView):

    def initial(self, request, *args, **kwargs):
        permission_classes = [AllowAny]

    def post(self, request):
        Book(title=request.data['title']).save()
        return Response({'POST': 'Books: Hello World!'}, 200)
