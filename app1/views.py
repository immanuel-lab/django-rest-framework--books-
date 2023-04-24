from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Book
from .serializers import BookSerializer

from rest_framework import status



@api_view(['GET','POST'])
def books_api(request):
    qs=Book.objects.all()
    serializer=BookSerializer(qs,many=True)
    return Response(serializer.data)


@api_view(['POST'])
def create_book(request):
        serializer=BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors)
