from django.shortcuts import render
from cat_app.cat import Cat

cat = Cat()


def index_view(request):
    return render(request, 'index.html')
