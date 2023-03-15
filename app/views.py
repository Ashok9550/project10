from django.shortcuts import render

# Create your views here.
def operators(request):
    d={'a':10,'b':20,'c':30}
    return render(request,'operators.html',context=d)