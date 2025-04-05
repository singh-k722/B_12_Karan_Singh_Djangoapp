from django.shortcuts import render , redirect
from .models import *
# Create your views here.
def recepies(request):
    if request.method == "POST":

        data = request.POST 
        r_image = request.FILES.get('r_image')
        r_name = data.get("r_name")
        r_description = data.get("r_description")
        
        Receipe.objects.create(
            r_image = r_image,
            r_name = r_name,
            r_description = r_description,
        )
        return redirect('/')
    
    queryset = Receipe.objects.all()
    context = {'receipes':queryset}
    return render(request, 'recipies.html' , context)


def update_rec(request , id):
    queryset  = Receipe.objects.get(id = id)
    
    if request.method == "POST":
        data = request.POST
        r_image = request.FILES.get('r_image')
        r_name = data.get("r_name")
        r_description = data.get("r_description")

        queryset.r_name = r_name
        queryset.r_description = r_description

        if r_image:
            queryset.r_image = r_image
        
        queryset.save()
        return redirect('/')
    context = {'receipe':queryset}
    return render(request, 'update_rec.html' , context)

def delete_receipe(request , id):
    queryset = Receipe.objects.get(id = id)
    queryset.delete()
    return redirect('/')