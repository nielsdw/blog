from rest_framework.response import Response
from rest_framework.decorators import api_view
from blog.serializers import BlogSerializer


@api_view(["GET"])
def index(request):
    serializer = BlogSerializer(data=request.data)
    if serializer.is_valid():
        return Response(request, status=201)
    return Response(data={}, status=200)


@api_view(["GET", "POST", "PATCH", "DELETE"])
def blogs():
    pass
