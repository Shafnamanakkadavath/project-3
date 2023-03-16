from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from moveiapp.models import movei
from .forms import moveiform


def film(request):
    act = movei.objects.all()
    context = {
        'list': act}
    return render(request, 'film.html', context)


def detail(request, movei_id):
    movei1 = movei.objects.get(id=movei_id)
    return render(request, "detail.html", {'movei': movei1})


def addmovei(request):
    if request.method == "POST":
        name = request.POST.get('name', )
        desc = request.POST.get('desc', )
        year = request.POST.get('year', )
        img = request.FILES['img']
        movei2 = movei(name=name, desc=desc, year=year, img=img)
        movei2.save()

    return render(request, 'add.html')


def update(request,id):
    movei3 = movei.objects.get(id=id)
    form = moveiform(request.POST or None, request.FILES, instance=movei3)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'edit.html', {'form': form, 'movei': movei3})
def delete(request,id):
    if request.method=='POST':
        movei4=movei.objects.get(id=id)
        movei4.delete()
        return redirect('/')
    return render(request,'delete.html')