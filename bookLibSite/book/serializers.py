from rest_framework import serializers
from .models import Author, Book, Parent, Child, SelfLink, Category


# For Book Serializer
class AuthorListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Author
        fields = ('id', 'name')

class BookSerializer(serializers.ModelSerializer):
    # authors = serializers.PrimaryKeyRelatedField(queryset=Author.objects.all(), many=True)
    authors = AuthorListSerializer(many=True, read_only=True)

    class Meta:
        model = Book
        fields = ('id', 'name', 'published', 'authors')

# for Author serializers
class BookListSerializer(serializers.ModelSerializer):

    class  Meta:
        model = Book
        fields = ('id', 'name')


class AuthorSerializer(serializers.ModelSerializer):
    book_list = BookListSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ('id', 'name', 'last_name', 'book_list')

# for Parent
class ChildListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Child
        fields = ('id', 'name')

class ParentSerializer(serializers.ModelSerializer):
    child_list = ChildListSerializer(many=True, read_only=True)

    class Meta:
        model = Parent
        fields =('id','name', 'child_list')

# For Child
class ParentListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Parent
        fields =('id','name')

class ChildSerializer(serializers.ModelSerializer):
    parent_list = ParentListSerializer(many=True, read_only=True)

    class Meta:
        model = Child
        fields = ('id', 'name', 'parent_list')

# For SelfLink
class SelflinkListSerializer(serializers.ModelSerializer):

    class Meta:
        model = SelfLink
        fields = ('name',)


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('category_name', )


class SelflinkSerializer(serializers.ModelSerializer):
    annon = SelflinkListSerializer(many=True, read_only=True)
    category = CategorySerializer(many=False, read_only=True)

    class Meta:
        model = SelfLink
        fields = ('id', 'name',  'annon', 'category')
