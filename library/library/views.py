from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.permissions import AllowAny
from rest_framework import status

from .models import Author, Book

import json


class AuthorsAPI(APIView):

    def initial(self, request, *args, **kwargs):
        permission_classes = [AllowAny]

    def get(self, request):

        if 'id' not in request.query_params:
            resp = Author.objects.values()
        else:
            id = request.query_params['id']
            resp = Author.objects.filter(id=id).values()

        return Response(resp, 200)

    def post(self, request):
        author = Author(name=request.data['name'],
                        gender=request.data['gender'])

        if 'books' in request.data:
            for book_id in json.loads(request.data['books']):
                book = Book.objects.get(id=book_id)
                author.books.add(book)
        author.save()

        return Response({'POST': 'Authors: Hello World!'}, 200)

    def put(self, request):
        old_author = Author.objects.get(id=request.query_params['id'])

        # load new data about author
        new_author = Author(id=old_author.id,
                            name=request.data['name'],
                            gender=request.data['gender'])

        if 'books' in request.data:
            for book_id in json.loads(request.data['books']):
                book = Book.objects.get(id=book_id)
                new_author.books.add(book)

        # replace all old author to new author
        old_author = new_author
        old_author.save()

        return Response({'PUT': 'Authors: Hello World!'}, 200)

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

    def delete(self, request):
        id = json.loads(request.query_params['id'])

        Author.objects.filter(id=id).delete()

        return Response({'DELETE': 'Authors: Hello World!'}, 200)


class BooksAPI(APIView):

    def initial(self, request, *args, **kwargs):
        permission_classes = [AllowAny]

    def get(self, request, pk=None):
        # read Request info
        print('Method:', request.method)
        print('Query params:', request.query_params)
        print('Headers:', request.headers)
        print('Body:', request.data)

        # generate Response
        response = Response(
            status=status.HTTP_200_OK,
            headers={},
            data={}
        )

        return response

    def post(self, request):
        Book(title=request.data['title']).save()
        return Response({'POST': 'Books: Hello World!'}, 200)
