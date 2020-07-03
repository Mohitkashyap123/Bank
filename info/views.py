from django.http import HttpResponse
from django.shortcuts import render
from .models import Bank

def index(request):
    products = Bank.objects.all()
    if len(products) == 0 :
        add_data()
    return render(request, 'index.html')

def result(request) :
    fifsc = None
    fname = None
    fcity = None
    print("result start")
    fifsc = request.GET.get('ifsc')
    print(fifsc)
    if fifsc is None :
        fname = str(request.GET.get('name')).strip()
        fcity = str(request.GET.get('city')).strip()
        print("Before")
        print(fname,fcity)
        print("After")
        t = fname.split(' ')
        branches = Bank.objects.filter(name__startswith=t[0], city=fcity)
        
        print(branches)
        params = {'option' : 0 , 'brnchs' : branches}
        return render(request, 'result.html', params)
        #return HttpResponse("this is name branch search")
    else :
        print("result called")
        mybank = Bank.objects.get(ifsc = fifsc)
        print(mybank)
        params = {'option' : 1 , 'bname' : mybank}
        return render(request, 'result.html', params)

def add_data() :
    #import os
    #module_dir = os.path.dirname(os.path.realpath(data.txt))  
    #file_path = os.path.join(module_dir, 'data.txt')   #full path to text.
    f = open("C:/Users/hp/Desktop/django/Bank/info/static/data.txt", 'r')
   # f = open('data.txt', 'r')  
    for line in f:
        try :  
            line =  line.split('"')
            first = line[0].split(',')
            sec = line[2].split(',')  
            product = Bank()  
            product.ifsc = first[0]
            product.bank_id = first[1]
            product.branch = first[2]
            product.address = line[1]
            product.city = sec[1]
            product.district = sec[2]
            product.state = sec[3]
            product.name = sec[4] 
   
            product.save()  

        except :
            continue

    f.close()
    