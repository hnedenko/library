from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from .models import Author, Book

import json


class AuthorsAPI(APIView):

    def initial(self, request, *args, **kwargs):
        permission_classes = [AllowAny]

    def post(self, request):
        Author(name=request.data['name'],
               gender=request.data['gender']).save()
        return Response({'POST': 'Authors: Hello World!'}, 200)
