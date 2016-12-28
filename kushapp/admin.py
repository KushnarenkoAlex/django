from django.contrib import admin

from .models import Author, Book

#This file allows us to customize our admin form.

admin.site.register(Book)

#django syntax that allows add bunch of books with adding an author
class BookInline(admin.StackedInline):
    model = Book
    extra = 3


class AuthorAdmin(admin.ModelAdmin):
	#splitting form inputs into separate fieldsets.
    fieldsets = [
        (None,               {'fields': ['author_name']}),
        ('Birth date', {'fields': ['birth_date']}),
    ]
	#allows edit book entity on author page. by default shows 3 fieldsets for books
    inlines = [BookInline]
	#define fields that we need to displays on Authors page for every Author.
    list_display = ('author_name', 'birth_date')
	#adding filter by fiels birth_date for authors page.
    list_filter = ['birth_date']
	#adding search functionality that allow seaching necessary text among authors names.
    search_fields = ['author_name']

#We need to call this function to change admin options for a model.
admin.site.register(Author, AuthorAdmin)

