
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('', include('book_api.urls')),
    path('books/', include('book_api.urls')),
    path('admin/', admin.site.urls),
]
