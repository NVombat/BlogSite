from django.shortcuts import render

posts = [
    {
        'author':'Nikhill Vombatkere',
        'title':'BlogPost 1',
        'content':'First Post Content',
        'date_posted':'July 27, 2021'
    },
    {
        'author':'Karan Vombatkere',
        'title':'BlogPost 2',
        'content':'Second Post Content',
        'date_posted':'July 25, 2021'
    }
]

def home(request):
    context = {
        'posts':posts
    }
    return render(request, 'home.html', context)

def about(request):
    return render(request, 'about.html', {'title': "About"})