from django.db.models import Q
from rest_framework import viewsets

from .models import Author, Book, Parent, Child, SelfLink
from .serializers import AuthorSerializer, BookSerializer, ParentSerializer, ChildSerializer, SelflinkSerializer


def split_string(string):
    string_list = []
    string_list = string.split(',')
    return string_list

class AuthorViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be views or edited
    """
    queryset = Author.objects.all().order_by('name')
    serializer_class = AuthorSerializer


class BookViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be views or edited
    """
    queryset = Book.objects.all().order_by('name')
    serializer_class = BookSerializer


class ParentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be views or edited
    """
    queryset = Parent.objects.all().order_by('name')
    serializer_class = ParentSerializer

class ChildViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be views or edited
    """
    queryset = Child.objects.all().order_by('name')
    serializer_class = ChildSerializer


class SelflinkViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be views or edited
    """
    queryset = SelfLink.objects.all().order_by('name')
    serializer_class = SelflinkSerializer

    def get_queryset(self):
        queryset = SelfLink.objects.all()
        self_name = self.request.query_params.get('name', None)
        category =self.request.query_params.get('category', None)

        if self_name:
            if self_name is not None:
                queryset = queryset.filter(name=self_name)
            return queryset
        elif category:
            if category is not None:
                # Check whether there is multiple values seperated  by comma ','
                if  ',' in category:
                    # Split the values seperated by comma ',' into a list
                    category_list = split_string(category)
                    # Create a query_list using category_list by list comprehension
                    query_list = [Q(category__category_name__iexact=cat_obj) for cat_obj in category_list]
                    # Pop the elements value of the query_list
                    query_combined = query_list.pop()
                    # Combine the elements to make the required query object
                    for item in query_list:
                        query_combined |= item
                    queryset = queryset.filter(query_combined).order_by('id')
                    return queryset
                else:
                    queryset = queryset.filter(category__category_name__iexact=category).order_by('-id')
                    return queryset
            return queryset
        return queryset
