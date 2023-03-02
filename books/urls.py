from django.urls import path

from . import views
app_name = 'books'

urlpatterns = [
    path('get_books', views.BooksListRetrieveAPiView.as_view(), name='get_books'),
]