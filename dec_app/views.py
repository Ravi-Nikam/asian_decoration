from django.shortcuts import render
from .models import Category_table
# Create your views here.
def home(request):
    cat=Category_table.objects.all()
    return render(request , 'index.html', {'cate': cat})

def registration(request):
    return render(request, 'registration.html')