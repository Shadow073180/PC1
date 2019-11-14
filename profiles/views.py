from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from .models import User, Pet, Match
from .forms import UserForm

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

