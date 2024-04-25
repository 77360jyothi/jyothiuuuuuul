from django.contrib import messages
from django.shortcuts import HttpResponse
from django.shortcuts import render, redirect
from .models import Movie
from . forms import MovieForm


# Create your views here.


def index(request):
    movie=Movie.objects.all()
    context={'movie_list':movie}
    return render(request,"index.html",context)


def detail(request,movie_id):
    movie=Movie.objects.get(id=movie_id)
    return render(request,"detail.html",{'movie':movie})

def add_movie(request):
    if request.method=="POST":
        name=request.POST.get('name',)
        desc=request.POST.get('desc', )
        year=request.POST.get('year', )
        img=request.FILES['img']
        movie=Movie(name=name,desc=desc,year=year,img=img)
        movie.save()

    return render(request,'add.html')


def update(request,id):
    movie=Movie.objects.get(id=id)
    form=MovieForm(request.POST or None, request.FILES, instance=movie)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form,'movie':movie})


def delete(request,id):
    if request.method=='POST':
        movie=Movie.objects.get(id=id)
        movie.delete()
        return redirect('/')
    return render(request,'delete.html')






def add_item_view(request):
    if request.method == 'POST':
        # Handle form submission
        name = request.POST.get('name')
        year = request.POST.get('year')
        img = request.FILES.get('image')
        desc = request.POST.get('description')

        if name and year and img and desc:
            # Save the data to the database
            Movie.objects.create(name=name, year=year, img=img, desc=desc)
            messages.success(request, 'Movie added successfully.')
            return redirect('/')
        else:
            messages.error(request, 'Please fill in all the fields.')
            return render(request, 'add_item.html')
    else:
        return render(request, 'add_item.html')
