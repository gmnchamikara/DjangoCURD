from django.shortcuts import render, redirect
from django.contrib import admin
from .models import Book
from .forms import BookCreate
from django.http import HttpResponse

# Register your models here.
admin.site.register(Book)

def index(request):
    shelf =  Book.objects.all()
    return render(request,  'book/library.html', {'shelf': shelf})

def upload(request):
    upload = BookCreate()
    if request.method == 'POST':
        upload = BookCreate(request.POST, request.FILES)
        if upload.is_valid():
            upload.save()
            return redirect('index')
        else:
            return HttpResponse("""Something went Wrong. Please reload the webpage 
                                by clicking <a href="{{url:'index'}}>Reload</a>" """)
    else:
        return render(request, 'book/upload_form.html', {'upload_from': upload})
    
def update_book(request, book_id):
    book_id = int(book_id)
    try:
        book_sheif = Book.objects.get(id = book_id)
    except Book.DoesNotExist
