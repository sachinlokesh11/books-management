from django.shortcuts import render
from rest_framework import views
import pandas as pd
# Create your views here.
from rest_framework.permissions import IsAuthenticated


class BooksListRetrieveAPiView(views.APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        rows = request.GET.get('q', None)
        df = pd.read_csv('static/books.csv')
        df = df.fillna('')
        if rows:
            row_data = df.loc[:rows]
            value = row_data.to_dict(orient='records')
        else:
            value = df.to_dict(orient='records')

        return render(request, 'books/index.html', {'books': value})

