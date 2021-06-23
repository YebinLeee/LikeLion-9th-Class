from django.shortcuts import render

def welcome (request):
    return render(request, 'welcome.html')

def hello(request):
    userName=request.GET['name'] #welcome.html의 name을 가져옴
    return render(request, 'hello.html', {'userName':userName}) # 가져온 값을 hello.html을 통해 반환