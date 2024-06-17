from django.shortcuts import render
from .models import Books

def book_list(request):
    # Get all books using the custom model manager
    books = Books.new_objects.get_books_in_genre('fiction')
    return render(request, 'books/book_list.html', {'books': books})