from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_list, name='create'),
    path('<int:id>', views.book),
    # path('update/<int:id>', views.book_update, name='update'),
    # path('delete/<int:id>', views.book_delete, name='delete'),
    
    
]

# # localhost/books => GET, POST
#  localhost/books/2 => GET, PUT, DELETE