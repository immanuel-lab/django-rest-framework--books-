from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import BookSerializer

from rest_framework import status

from .models import Book

# @api_view(['GET'])
# def books_api(request):
#     qs=Book.objects.all()
#     serializer=BookSerializer(qs,many=True)
#     return Response(serializer.data)


# @api_view(['POST'])
# def create_book(request):
#         serializer=BookSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors)


@api_view(['GET','POST'])
def books_api(request):
    if request.method == 'GET':

        qs=Book.objects.all()
        serializer=BookSerializer(qs,many=True)
        return Response(serializer.data)
    if request.method == 'POST':
            serializer=BookSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors)




@api_view(['GET','DELETE','PUT'])
def booksall_api(request,pk):
    try:
        book=Book.objects.get(pk=pk)
    except:
        return Response({'error':"book doesn't exist"},status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':

        serializer=BookSerializer(book)
        return Response(serializer.data)

    if request.method == 'DELETE':
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    if request.method == 'PUT':
        
        serializer=BookSerializer(book,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

  