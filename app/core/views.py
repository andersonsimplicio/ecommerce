#config=utf-8
from django.shortcuts import render

def index(request):
    template='index.html'
    context = {
        'title':'little amazon'
    }
    return render(request,template,context=context)


