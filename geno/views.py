from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.
def home(request):
    return render(request, 'geno/new.html')

def password(request):
    charac = list('abcdefghijklmnopqrstuvwxyz')
    if request.GET.get('uppercase'):
        charac.extend(list('ABCDEFGHIJKLMNOPQRST'))
    if request.GET.get('numbers'):
        charac.extend(list('0123456789'))
    if request.GET.get('special'):
        charac.extend(list('~!@#$%|\/&*'))
    
    length = int(request.GET.get('length',12))
    newpassword = ''
    for i in range(length):
        newpassword += random.choice(charac)
    thispass = ''
    return render(request, 'geno/pass.html', {'password':newpassword})
def about(request):
    return render(request, 'geno/about.html')