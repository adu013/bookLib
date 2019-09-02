from django.shortcuts import render


from .models import Author, Book


def AuthorView(request):
    objects = Author.objects.all().order_by('name')
    context = {'objects': objects}
    return render(request, template_name='book/author.html', context=context)


def BookView(request):
    objects = Book.objects.all().order_by('name')
    context = {'objects': objects}
    return render(request, template_name='book/books.html', context=context)
