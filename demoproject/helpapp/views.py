from django.shortcuts import render

# Create your views here.
def index(req):
    data = { 'greetings': 'This is the help page.' }
    return render(req, 'helpindex.html', context=data)