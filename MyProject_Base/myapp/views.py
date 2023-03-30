from django.shortcuts import render
from django.http import HttpResponse
from .forms import df
from .models import Details
# # Create your views here.
# def Helloapp(request):
#     #return HttpResponse("<b><h1 align=center>Hello Django World</h1></b><hr><p align=center><b>My First Django Webapp</b></p>")
#     return render(request, "home.html")

#Insert data
def Add(request):
    if request.method == "POST":
        name1 = request.POST.get("name")
        email1 = request.POST.get("email")
        con1 = request.POST.get("contact")
        print(name1, email1,con1)
        obj=Details.objects.create(name=name1, email=email1, contact=con1)
        obj.save()
    return render(request, 'home.html')

#Display Data
def retrieve(request):
    details=Details.objects.all()
    return render(request,'Showdata.html',{'details_key':details})

#Edit data
def edit(request,idp):
    object=Details.objects.get(id=idp)
    return render(request,'edit.html',{'objectp':object})

#Update Data
def update(request,idu):
    object=Details.objects.get(id=idu)
    form=df(request.POST,instance=object)
    if form.is_valid:
        form.save()
        details=Details.objects.all()
        return render(request,'home.html')

#Delete Data
def delete(request,idd):
    member=Details.objects.get(id=idd)
    member.delete()
    return render(request,'home.html')