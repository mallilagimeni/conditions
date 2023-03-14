from django.shortcuts import render

# Create your views here.
def cond(request):
    d={'name':'malli'}
    return render(request,'cond.html',context=d)