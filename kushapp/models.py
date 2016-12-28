from django.db import models

class Author(models.Model):
    author_name = models.CharField(max_length=200)
    birth_date = models.DateTimeField('birth_date')
    
class Book(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    book_name = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date')
