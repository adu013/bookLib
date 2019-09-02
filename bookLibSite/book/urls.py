from django.urls import include, path
from rest_framework import routers

from .views import AuthorView, BookView
from .api import AuthorViewSet, BookViewSet, ParentViewSet, ChildViewSet, SelflinkViewSet

app_name = 'book'

routers = routers.DefaultRouter()
routers.register(r'authors', AuthorViewSet)
routers.register(r'books', BookViewSet)
routers.register(r'parent', ParentViewSet)
routers.register(r'child', ChildViewSet)
routers.register(r'selflink', SelflinkViewSet)

urlpatterns = [
    path('api/', include(routers.urls)),
    path('authors/', AuthorView, name='author'),
    path('books/', BookView, name='book'),
]
