from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from .models import Book

import psycopg2


def db_execute(injection):
    connection = psycopg2.connect(dbname='library',
                                  user='postgres',
                                  password='a1423578690',
                                  host='localhost')
    cursor = connection.cursor()

    cursor.execute(injection)
    records = cursor.fetchall()

    cursor.close()
    connection.close()

    return records


class BooksAPI(APIView):

    def initial(self, request, *args, **kwargs):
        permission_classes = [AllowAny]

    def get(self, request):

        """
        book = Book(id="",
                    title="",
                    tags="",
                    authors_id="")
        book.save(force_insert=True)
        """

        return Response({'GET': 'Books: Hello World!'}, 200)

    def post(self, request):
        return Response({'POST': 'Books: Hello World!'}, 200)

    def patch(self, request):
        return Response({'PATCH': 'Books: Hello World!'}, 200)

    def put(self, request):
        return Response({'PUT': 'Books: Hello World!'}, 200)

    def delete(self, request):
        return Response({'DELETE': 'Books: Hello World!'}, 200)
