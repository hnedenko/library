from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from .models import Author

import json

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


class AuthorsAPI(APIView):

    def initial(self, request, *args, **kwargs):
        permission_classes = [AllowAny]

    def get(self, request):
        print(request.query_params)
        all_authors = Author.objects.all().values()
        return Response(list(all_authors), 200)

    def post(self, request):
        Author(name=request.data['name'],
               gender=request.data['gender'],
               books_id=json.loads(request.data['books_id'])).save()
        return Response({'POST': 'Authors: Hello World!'}, 200)

    def patch(self, request):
        return Response({'PATCH': 'Authors: Hello World!'}, 200)

    def put(self, request):
        id = request.data['id']
        Author.objects.filter(id=id)
        return Response({'PUT': 'Authors: Hello World!'}, 200)

    def delete(self, request):
        id = request.data['id']
        Author.objects.filter(id=id).delete()
        return Response({'DELETE': 'Authors: Hello World!'}, 200)
