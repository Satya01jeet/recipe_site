from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    people = [
        {'name': 'Satyajeet Sau', 'age': 22},
        {'name': 'Anwesha Sen', 'age': 19},
        {'name': 'Abhishek Brijwasi', 'age': 22},
        {'name': 'Satyakant Mishra', 'age': 21},
        {'name': 'Saurabh Prashad', 'age': 21},
        {'name': 'Dhruv Kumar', 'age': 21},
        {'name': 'Subhankar Dhamali', 'age': 24},
        {'name': 'Akash Jyoti', 'age': 25},
        {'name': 'Aniket Das', 'age': 25},
    ]
    return render(request, 'home/index.html', context={'people': people})

def about(request):
    return render(request, 'home/about.html')

def contact(request):
    return render(request, 'home/contact.html')
