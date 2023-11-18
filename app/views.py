from django.shortcuts import render

# Create your views here.
def data_render(request):
    data='This data is our assumption'
    d={'assumption':data}
    return render(request,'data_render.html',context=d)


def login(request):
    data='welcome to our login page'
    d={'name':data}
    return render(request,'login.html',d)
