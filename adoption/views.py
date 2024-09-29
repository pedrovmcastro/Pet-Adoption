from django.shortcuts import render, redirect

from .models import Pet, Interest
from .forms import InterestForm

# Create your views here.
def index(request):
    pets = Pet.objects.all()

    context = {"pets": pets}
    return render(request, "adoption/index.html", context)


def pet_details(request, pet_id):
    pet = Pet.objects.get(id=pet_id)

    if request.method == "POST":
        form = InterestForm(request.POST)
        if form.is_valid():
            Interest.objects.create(
                pet=pet, 
                email=form.cleaned_data['email'],
                message=form.cleaned_data.get('message', '')
                )
            return redirect("adoption:pet_list")
    else:
        form = InterestForm()

    context = {"pet": pet, "form": form}
    return render(request, 'adoption/pet_details.html', context)
