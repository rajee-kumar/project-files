from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse,JsonResponse

from rest_framework.response import Response

from .models import DataApi
from .models import student
from .models import emp
from .serializer import empserializer
from rest_framework.decorators import api_view
from .serializer import GeeksModelSerializer
from .serializer import studentModelSerializer
from rest_framework import status
    
def home(request):  
    return HttpResponse("<h2>Hello, Welcome to Django!</h2>")  

def about(request):  
    return HttpResponse("<h2>Hello, About to Django!</h2>")  

def contact(request):  
    return HttpResponse("<h2>Hello, contact to Django!</h2>")  
def first_pro(request):
    return HttpResponse("<h2>welcome to django project</h2>")

def add_two(request):
    
    return HttpResponse('i am learning django for web ')
def greet(request):
    return HttpResponse('<h1>Hello Namaskar desto kya hall hai</h1>')
def course(request,courseid):
    return HttpResponse(courseid)
def mynew(request):
    data={'title1':'my new title','first':'this is my django project'
     ,'course':['php','java','c','html']}
    return render(request,"index.html",data)
def logins(request):
    return render(request,"login.html")
@api_view(['GET','POST'])
def sample_model(request):
    if request.method=='GET':

    
        datapii=DataApi.objects.all()
        serializer=GeeksModelSerializer(datapii,many=True)
        return JsonResponse({'data':serializer.data},safe=False)
    if request.method=='POST':
        serializer=GeeksModelSerializer(data=request.data)
        if serializer.is_valid():
           serializer.save()
           return Response(serializer.data,status=status.HTTP_201_CREATED)
@api_view(['GET','POST'])
def sample_model1(request):
    if request.method=='GET':

    
        stu_data=student.objects.all()
        serializer=studentModelSerializer(stu_data,many=True)
        return Response({'data':serializer.data})

    if request.method == 'POST':
        serializer = studentModelSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'data':serializer.data}, status=status.HTTP_201_CREATED)
    # Handle invalid data case if needed
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#-------------------
# @api_view(['GET','POST'])   
# def emp_details(request):
#     if request.method=='GET':
#         empdata=emp.objects.all()
#         serializer=empserializer(empdata,many=True)
#         return Response({'data':serializer.data},content_type='application/json')
#     if request.method=='POST':
#         serializer=empserializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response({'data':serializer.data},status=status.HTTP_201_CREATED,content_type='application/json')
#     return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST,content_type='application/json')


#-----------------------
@api_view(['GET', 'POST'])   
def emp_details(request):
    if request.method == 'GET':
        empdata = emp.objects.all()
        serializer = empserializer(empdata, many=True)
        return Response({'data': serializer.data}, content_type='application/json')
    
    elif request.method == 'POST':
        serializer = empserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'data': serializer.data}, status=status.HTTP_201_CREATED, content_type='application/json')
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST, content_type='application/json')

