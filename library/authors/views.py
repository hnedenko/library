from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny


class AuthorsAPI(APIView):

    def initial(self, request, *args, **kwargs):
        permission_classes = [AllowAny]

    def get(self, request):
        return Response({'GET': 'Authors: Hello World!'}, 200)

    def post(self, request):
        return Response({'POST': 'Authors: Hello World!'}, 200)

    def patch(self, request):
        return Response({'PATCH': 'Authors: Hello World!'}, 200)

    def put(self, request):
        return Response({'PUT': 'Authors: Hello World!'}, 200)

    def delete(self, request):
        return Response({'DELETE': 'Authors: Hello World!'}, 200)
