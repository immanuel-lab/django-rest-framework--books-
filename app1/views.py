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

# @api_view(['GET'])
# def get_user(request):
#     qs=models.BookNewNew.objects.all()
#     serializer= serializers.BookNewNewSerializer(qs,many=True)
#     return Response(serializer.data, status=status.HTTP_200_OK)



# @api_view(['GET'])
# def get_user(request):
#     qs=models.BookNewNew.objects.get(name="franklin")
#     serializer= serializers.BookNewNewSerializer(qs)
#     return Response(serializer.data, status=status.HTTP_200_OK)
#     # return Response({'message':'successful'}, status=status.HTTP_200_OK)



# count()
# @api_view(['GET'])
# def get_user(request):
#     qs=models.BookNewNew.objects.count()
#     # serializer= serializers.BookNewNewSerializer(qs)
#     return Response(qs, status=status.HTTP_200_OK)
#     # return Response({'message':'successful'}, status=status.HTTP_200_OK)
    



# @api_view(['GET'])
# def get_user(request):
#     # qs=models.BookNewNew.objects.exclude(name='franklin')
#     qs=models.BookNewNew.objects.filter(name='franklin').delete()
#     serializer= serializers.BookNewNewSerializer(qs,many=True)
#     return Response(serializer.data, status=status.HTTP_200_OK)



# @api_view(['GET'])
# def get_user(request):
#     # Retrieve the object to delete
#     bookNews_to_delete = models.BookNewNew.objects.filter(name='franklin')

#     # Check if any bookNews match the filter criteria
#     if bookNews_to_delete.exists():
#         # Delete the matching bookNews
#         bookNews_to_delete.delete()
#         return Response({'message': 'BookNews deleted successfully'}, status=status.HTTP_200_OK)
#     else:
#         return Response({'message': 'No bookNews found matching the filter criteria'}, status=status.HTTP_404_NOT_FOUND)
    


# @api_view(['GET','POST','DELETE'])
# def get_user(request):
#     if request.method == 'GET':
#          qs=models.BookNew.objects.filter(name='james')
#          serializer=serializers.BookNewSerializer(qs,many=True)
#          return Response(serializer.data, status=status.HTTP_200_OK)

#     if request.method == 'POST':
#             serializer=serializers.BookNewSerializer(data=request.data)
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response(serializer.data,status=status.HTTP_201_CREATED)
#             else:
#                 return Response(serializer.errors)
            
#     if request.method=='DELETE':
#          qs=models.BookNew.objects.filter(name='james')
#          if qs.count()>1:
#               qs.first().delete()
#               return Response({'message:james deleted'})

  
