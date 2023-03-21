from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.db.models import Q
from .forms import *

# Create your views here.
def blog(request):
    text = Blog.objects.all()

    if request.method == 'POST':
        if 'button_clicked' in request.POST:
            id = request.POST.get('id-post')
            fav = get_object_or_404(Blog, pk=id)
            fav.favorite = True
            fav.save()
            return redirect("blog")

        else: # Обработка формы создания поста
            form = CreateForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect("blog")
            else:
                error = "Ошибка"
                form = CreateForm()
    else:
        form = CreateForm()
        error = ''

    data = {
        'text': text,
        'error': error,
        'form': form,
    }
    return render(request, 'blog/blog.html', data)

def favorite(request):
    text = Blog.objects.filter(Q(favorite=True))
    data = {
        'text': text,
    }
    return render(request, 'blog/fav.html', data)

def profile(request):
    return render(request, 'blog/profile.html')

def about(request):
    return render(request, 'blog/about.html')

def contact(request):
    return render(request, 'blog/contact.html')

def portfolio(request):
    return render(request, 'blog/portfolio.html')

