from django.contrib.auth.models import User, Permission, Group
from django.contrib.contenttypes.models import ContentType
from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout
    )
from django.shortcuts import render

from Bish_vip.models import Post
from .forms import UserLoginForm, UserRegisterForm
# Create your views here.

def login_view(request):
    title = "Войти"
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username=username, password=password)
        login(request, user)
        return  redirect("/posts/profile")

    return render(request, "accaunt_form.html", {"form":form, "title": title})


def register_view(request):
    title = "Регистрация"
    form = UserRegisterForm(request.POST or None)

    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get("password")
        user.set_password(password)
        user.save()
        user_gains_perms(request, user_id=user.id)
        new_user = authenticate(username=user.username, password=password)
        login(request, new_user)
        return redirect("/posts/profile")
    context = {
        'form' : form,
        'title' : title

    }
    return render(request, "accaunt_form.html", context)



def logout_view(request):
    logout(request)
    return redirect("/posts")

def profile_view(request):
    if not request.user.is_authenticated:
        raise Http404
    title = "Мой профиль"
    user = request.user
    data_list = Post.objects.all().filter(user=user.id)
    context = {
        'user' : user,
        'title' : title,
        'posts': data_list
    }
    return render(request, "profile.html", context)

def user_gains_perms(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    # any permission check will cache the current set of permissions
    user.has_perm('Bish_vip.change_post')
    user.has_perm('Bish_vip.add_post')
    user.has_perm('Bish_vip.delete_post')
    user.has_perm('comments.add_comment')
    content_type = ContentType.objects.get_for_model(Post)

    perm_change = Group.objects.get(name='def_user')

    user.groups.add(perm_change)

    # Checking the cached permission set
    user.has_perm('Bish_vip.change_post')  # False
    user.has_perm('Bish_vip.add_post')
    user.has_perm('Bish_vip.delete_post')
    user.has_perm('comments.add_comment')

    # Request new instance of User
    # Be aware that user.refresh_from_db() won't clear the cache.
    user = get_object_or_404(User, pk=user_id)

    # Permission cache is repopulated from the database
    user.has_perm('Bish_vip.change_post')  # True
    user.has_perm('Bish_vip.add_post')
    user.has_perm('Bish_vip.delete_post')
    user.has_perm('comments.add_comment')