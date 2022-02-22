from django.http import HttpResponse
from django.shortcuts import render, redirect
from . models import movie
from . forms import  movieform
# Create your views here.
def fun(request):
    obj=movie.objects.all()
    return render(request,"hello.html",{'result':obj})

def details(request,movie_id):
    mov=movie.objects.get(id=movie_id)
    return render(request,"details.html", {'movies':mov})
def register(request)  :
    if request.method=='POST':
        name=request.POST.get('name',)
        desc = request.POST.get('desc',)
        year = request.POST.get('year',)
        img = request.FILES['img']
        mov=movie(name=name,desc=desc,year=year,img=img)
        mov.save()

    return render(request,'register.html')
def edit(request,id)    :
    mov=movie.objects.get(id=id)
    f=movieform(request.POST or None,request.FILES,instance=mov)
    if f.is_valid():
        f.save()
        return redirect('/')
    return render(request,'edit.html',{'fo':f,'movi':mov})
def delete(request,id)   :
    if request.method=='POST':


        de=movie.objects.get(id=id)
        de.delete()
        return redirect('/')
    return render(request,'delete.html')




    # return HttpResponse("movie no is %s" % movie_id)
# def details(request,movie_id):
#     return HttpResponse("id no is %s" % movie_id)
