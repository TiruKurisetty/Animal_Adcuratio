from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from app.forms import *
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from rest_framework.viewsets import ViewSet
from app.serializers import *
from rest_framework.response import Response
from django.views.generic import CreateView



def home(request):

    if request.session.get('username'):
        username=request.session.get('username')
        d={'username':username}
        return render(request,'home.html',d)
    

    return render(request,'home.html')



def registration(request):
    ufo=UserForm()
    d={'ufo':ufo}
    if request.method=='POST':
        ufd=UserForm(request.POST)
        if ufd.is_valid():
            NSUO=ufd.save(commit=False)
            password=ufd.cleaned_data['password']
            NSUO.set_password(password)
            NSUO.save()
            return render(request,'home.html')
        else:
            return HttpResponse('Not valid')

    return render(request,'registration.html',d)


def user_login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']

        AUO=authenticate(username=username,password=password)
        if AUO and AUO.is_active:
            login(request,AUO)
            request.session['username']=username
            return HttpResponseRedirect(reverse('home'))
        else:
            return HttpResponse('Invalid username or password') 
        
    return render(request,'user_login.html')

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))
    


class AnimalData(ViewSet):
    def list(self,request):
        ADO=Animals.objects.all()
        SJD=AnimalSeriallizer(ADO,many=True)
        d={'data':SJD.data}
        return render(request,'list.html',d)

    def retrieve(self,request,pk):
        TO=Animals.objects.get(pk=pk)
        SDO=AnimalSeriallizer(TO)
        return Response(SDO.data)

    def update(self,request,pk):
        SPO=Animals.objects.get(pk=pk)
        SPD=AnimalSeriallizer(SPO,data=request.data)
        if SPD.is_valid():
            SPD.save()
            return Response({'Updated':'Product is updated'})
        else:
            return Response({'Failed':'Prodct is Not Updated'})
    
    def partial_update(self,request,pk):
        SPO=Animals.objects.get(pk=pk)
        SPD=AnimalSeriallizer(SPO,data=request.data,partial=True)
        if SPD.is_valid():
            SPD.save()
            return Response({'Updated':'Product is updated'})
        else:
            return Response({'Failed':'Prodct is Not Updated'})
    def destroy(self,request,pk):
        Animals.objects.get(pk=pk).delete()
        return Response({'Deleted':'Product is deleted'})
    



def animals_form(request):
    d={'UO' : AnimalsForm()}
    if request.method == 'POST' and request.FILES:
        UOD=AnimalsForm(request.POST,request.FILES) 
        if UOD.is_valid():
            UOD.save()
            return HttpResponse('done')
    return render(request,'animals_form.html',d)