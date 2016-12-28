from django.db import models

#These models have one-to-many dependency. 
class Author(models.Model):
    author_name = models.CharField(max_length=200)
    birth_date = models.DateTimeField('birth_date')
    
class Book(models.Model):
	#on_delete CASCADE means that all books will be deleted if parent entity will be deleted.
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    book_name = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date')
