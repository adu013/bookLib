from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100, default="")
    last_name = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Book(models.Model):
    authors = models.ManyToManyField(Author, related_name="book_list", blank=True, null=True)
    name = models.CharField(max_length=100, default="")
    published = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Parent(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Child(models.Model):
    name = models.CharField(max_length=100)
    parent_list = models.ManyToManyField('Parent',related_name='child_list', blank=True, null=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    category_name = models.CharField(max_length=100, primary_key=True)

    def __str__(self):
        return  self.category_name


class SelfLink(models.Model):
    name = models.CharField(max_length=100)
    annon = models.ManyToManyField('SelfLink', related_name='annon_list', blank=True, null=True)
    category = models.ForeignKey('Category', related_name='cat', on_delete=models.SET_NULL, null=True, blank=True, default="")

    def __str__(self):
        return self.name
