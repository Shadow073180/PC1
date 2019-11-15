from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from .models import User, Pet, Match
from .forms import UserForm, PetForm

# Create your views here.
def user_list(request):
    users = User.objects.all()
    return render(request, './users/user_list.html', {'users': users})

def user_detail(request, user_id):
    user = get_object_or_404(User, id=user_id)
    return render(request, './users/user_detail.html', {'user':user})

def new_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
                user = form.save(commit=False)
                user.save()
                return redirect('user_detail', user_id=user.id)
    else:
        form = UserForm()
    return render(request, 'users/user_form.html', {'form': form, 'type_of_request': 'New'})


def edit_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
                user = form.save(commit=False)
                user.save()
                return redirect('user_detail', user_id=user.id)
    else:
        form = UserForm(instance=user)
    return render(request, 'users/user_form.html', {'form': form, 'type_of_request': 'Edit'})

def delete_user(request, user_id):
    if request.method == "POST":
        user = get_object_or_404(User, id=user_id)
        user.delete()
    return redirect('user_list')

# ---------------------------------------Pets CRUD

def pets_list(request, user_id):
    user = get_object_or_404(User, id=user_id)
    pets = Pet.objects.all()
    return render(request, './pets/pets_list.html' ,{'user': user, 'pets': pets})

def pet_detail(request, user_id, pet_id):
    user = get_object_or_404(User, id=user_id)
    pet = get_object_or_404(Pet, id=pet_id)
    return render(request, './pets/pet_detail.html', {'user':user , 'pet':pet})

def new_pet(request, user_id):
    if request.method == "POST":
        form = PetForm(request.POST)
        if form.is_valid():
            pet = form.save(commit=False)
            pet.save()
        return redirect('pet_detail', user_id=pet.user.id, pet_id=pet.id)
    else:
        form = PetForm()
    return render(request, 'pets/pet_form.html', {'form': form, 'type_of_request': 'New'})

def edit_pet(request, user_id, pet_id):
    user = get_object_or_404(User, id=user_id)
    pet = get_object_or_404(Pet, id=pet_id)
    if request.method == "POST":
        form = PetForm(request.POST, instance=pet)
        if form.is_valid():
            pet = form.save(commit=False)
            pet.save()
            return redirect('pet_detail', user_id=user.id, pet_id=pet.id)
    else:
        form = PetForm(instance=pet)
    return render(request, 'pets/pet_form.html', {'form': form, 'type_of_request': 'Edit'})

def delete_pet(request, user_id, pet_id):
    if request.method == 'POST':
        pet = get_object_or_404(Pet, id=pet_id)
        pet.delete()
    return redirect('pets_list', user_id = user_id)

#  ----------------------------------------Match

def match_list(request, user_id):
    user = get_object_or_404(User, id=user_id)
    matches = Match.objects.all()
    return render(request, './matches/match_list.html', {'user':user, 'matches': matches})


