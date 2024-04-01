from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny


class BooksAPI(APIView):

    def initial(self, request, *args, **kwargs):
        permission_classes = [AllowAny]

    def get(self, request):
        return Response({'GET': 'Books: Hello World!'}, 200)

    def post(self, request):
        return Response({'POST': 'Books: Hello World!'}, 200)

    def patch(self, request):
        return Response({'PATCH': 'Books: Hello World!'}, 200)

    def put(self, request):
        return Response({'PUT': 'Books: Hello World!'}, 200)

    def delete(self, request):
        return Response({'DELETE': 'Books: Hello World!'}, 200)
