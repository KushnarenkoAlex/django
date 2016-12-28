from django.contrib import admin

from .models import Author, Book

admin.site.register(Book)

class BookInline(admin.StackedInline):
    model = Book
    extra = 3


class AuthorAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['author_name']}),
        ('Birth date', {'fields': ['birth_date']}),
    ]
    inlines = [BookInline]
    list_display = ('author_name', 'birth_date')
    list_filter = ['birth_date']
    search_fields = ['author_name']
    
admin.site.register(Author, AuthorAdmin)

