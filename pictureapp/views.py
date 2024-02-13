from django.http import HttpResponse
from django.shortcuts import render, redirect
from . models import Picture
from . forms import PictureForm
# Create your views here.
def index(request):
    picture=Picture.objects.all()
    context={
        'picture_list':picture
    }
    return render(request,'index.html',context)

def detail(request,picture_id):
    picture=Picture.objects.get(id=picture_id)
    return render(request,"detail.html",{'picture':picture})

def add_picture(request):
    if request.method=="POST":
        name=request.POST.get('name',)
        desc = request.POST.get('desc',)
        year = request.POST.get('year',)
        actors = request.POST.get('actors',)
        category = request.POST.get('category',)
        link = request.POST.get('link',)
        img = request.FILES['img']
        picture=Picture(name=name,desc=desc,year=year,actors=actors,category=category,link=link,img=img)
        picture.save()

    return render(request,'add.html')

def edit(request,id):
    picture=Picture.objects.get(id=id)
    form=PictureForm(request.POST or None, request.FILES,instance=picture)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form,'picture':picture})

def delete(request,id):
    if request.method=='POST':
        picture=Picture.objects.get(id=id)
        picture.delete()
        return redirect('/')
    return render(request,'delete.html')