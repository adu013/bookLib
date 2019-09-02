from django.contrib import admin

from .models import Author, Book, Parent, Child, SelfLink, Category

# Register your models here.
admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Parent)
admin.site.register(Child)
admin.site.register(SelfLink)
admin.site.register(Category)
