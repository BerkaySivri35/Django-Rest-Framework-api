from django.shortcuts import render
from django.http import JsonResponse

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from book_api.models import Book
from book_api.serializer import BookSerializer

# Create your views here.

#GET ve POST u tek fonksiyon altında yazalım.
@api_view(['GET','POST'])
def book_list(request):
    if request.method == 'GET':
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True) 
        #dönüştürülecek olan db deki verileri gönderiyoruz.

        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors)




#GET, PUT, DELETE' i tek fonksiyon altında yazalım.
@api_view(['GET','PUT','DELETE'])
def book(request,id):
    try:
        book = Book.objects.get(pk=id)
        
    except:
        return Response({"error":"Kayıt Bulunamadı."}, status=status.HTTP_404_NOT_FOUND)

    

    if request.method == "GET":
        serializer = BookSerializer(book)
        return Response(serializer.data)
    
    elif request.method == "PUT":
        
        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    elif request.method == "DELETE":
        
        book.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)






# serialize