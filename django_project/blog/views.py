from django.shortcuts import render


posts = [
    {
        'author': 'HarryAF',
        'title': 'Blog Post',
        'content': 'First Post Content',
        'date_posted': 'Febuary 17, 2024'
    },
    {
        'author': 'AmethystAF',
        'title': 'Blog Post 2',
        'content': 'Second Post Content',
        'date_posted': 'Febuary 18, 2024'
    }
]

# Create your views here.
def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html',{'title': 'About'})
