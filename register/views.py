from django.shortcuts import render

def index(request):
    name='nanthagopal'
    context={'name':name}
    return render(request,'index.html',context)
