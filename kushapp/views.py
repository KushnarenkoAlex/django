from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.template import loader
from .models import Author

def index(request):
    author_list = Author.objects.order_by('-birth_date')[:5]
    template = loader.get_template('kushapp/index.html')
    context = {
        'author_list': author_list,
    }
    return HttpResponse(template.render(context, request))

def detail(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    return render(request, 'kushapp/details.html', {'author': author})

def books(request, author_id):
    return HttpResponse("You're looking at the books of author %s." % author_id)

def update(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    new_name = request.POST['new_name']
    author.author_name=new_name
    author.save()
    return render(request, 'kushapp/details.html', {'author': author})

