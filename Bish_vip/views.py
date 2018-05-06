from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import get_object_or_404, HttpResponseRedirect, redirect
from django.shortcuts import render, Http404
from Services.models import *
from comments.CommentForms import CommentForm
from comments.models import Comment
from .PostForms import PostForm
from .models import Post


# Create your views here.
def post_create(request):
    # if not request.user.is_staff or not request.user.is_superuser:
    #     raise Http404()
    if not request.user.is_authenticated:
        raise Http404
    form = PostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        # print(form.cleaned_data)
    context = {
        "form": form,
    }
    return render(request, "post_form.html", context)


def post_update(request, id=None):
    title = "Update"
    # if not request.user.is_stuff or not request.user.is_superuser:
    #     raise Http404
    instanse = get_object_or_404(Post, id=id)
    form = PostForm(request.POST or None, request.FILES or None, instance=instanse)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "title": title,
        "instence": instanse,
        "form": form,
    }
    return render(request, "post_form.html", context)


def post_delete(request, id=None):
    if not request.user.is_stuff or not request.user.is_superuser:
        raise Http404
    instance = get_object_or_404(Post, id=id)
    instance.delete()
    return redirect("Bish_vip:list")


def post_sort(request):
    data_list = Post.objects.all().order_by('update')
    post_pages = ""
    if data_list.count() > 0:
        paginator = Paginator(data_list, 5)  # Show 25 contacts per page
        page = request.GET.get('page')
        try:
            post_pages = paginator.page(page)
        except PageNotAnInteger:
            post_pages = paginator.page(1)
        except EmptyPage:
            post_pages = paginator.page(paginator.num_pages)
    # contacts = paginator.get_page(page)
    # comments = Comment.objects.filter_by_instance(get_object_or_404(Post, id=4))
    context = {
        "instance": data_list,
        "obj_list": post_pages,
        # "comment": comments,
    }
    return render(request, "post_list.html", context)


def post_home(request):
    data_list = Post.objects.all()
    post_pages = ""
    if data_list.count() > 0:
        paginator = Paginator(data_list, 5)  # Show 25 contacts per page
        page = request.GET.get('page')
        try:
            post_pages = paginator.page(page)
        except PageNotAnInteger:
            post_pages = paginator.page(1)
        except EmptyPage:
            post_pages = paginator.page(paginator.num_pages)
    # contacts = paginator.get_page(page)
    # comments = Comment.objects.filter_by_instance(get_object_or_404(Post, id=4))
    context = {
        "instance": data_list,
        "obj_list": post_pages,
        # "comment": comments,
    }
    return render(request, "post_list.html", context)


def post_detail(request, id=None):
    instance = get_object_or_404(Post, id=id)
    if not request.user.is_authenticated:
        if not (instance.user_is_active and instance.admin_is_active):
            print("Not activate")
            raise Http404

    comment = Comment.objects.filter_by_instance(instance)
    initial_data = {
        "content_type": instance.get_content_type,
        "object_id": instance.id
    }
    comment_form = CommentForm(request.POST or None, initial=initial_data)
    if comment_form.is_valid():
        c_type = comment_form.cleaned_data.get("content_type")
        content_type = ContentType.objects.get(model=c_type)
        obj_id = comment_form.cleaned_data.get('object_id')
        content_data = comment_form.cleaned_data.get("content")
        # parent_id = request.POST.get("parent_id")
        parent_obj = None
        try:
            parent_id = int(request.POST.get("parent_id"))
        except:
            parent_id = None

        if parent_id:
            parent_qs = Comment.objects.filter(id=parent_id)
            if parent_qs.exists() and parent_qs.count() == 1:
                parent_obj = parent_qs.first()

        new_comment, created = Comment.objects.get_or_create(
            user=request.user,
            content_type=content_type,
            object_id=obj_id,
            content=content_data,
            parent=parent_obj,
        )
        return HttpResponseRedirect(new_comment.content_object.get_absolute_url())
    comments = instance.comments
    context = {
        "instance": instance,
        "comments": comments,
        "comment_form": comment_form,
    }
    return render(request, "detail.html", context)


def commentary(request, instance):
    initial_data = {
        "content_type": instance.get_content_type,
        "object_id": instance.id
    }
    comment_form = CommentForm(request.POST or None, initial=initial_data)
    if comment_form.is_valid():
        c_type = comment_form.cleaned_data.get("content_type")
        content_type = ContentType.objects.get(model=c_type)
        obj_id = comment_form.cleaned_data.get('object_id')
        content_data = comment_form.cleaned_data.get("content")
        # parent_id = request.POST.get("parent_id")
        parent_obj = None
        try:
            parent_id = int(request.POST.get("parent_id"))
        except:
            parent_id = None

        if parent_id:
            parent_qs = Comment.objects.filter(id=parent_id)
            if parent_qs.exists() and parent_qs.count() == 1:
                parent_obj = parent_qs.first()

            new_comment, created = Comment.objects.get_or_create(
                user=request.user,
                content_type=content_type,
                object_id=obj_id,
                content=content_data,
                parent=parent_obj,
            )
            return HttpResponseRedirect(new_comment.content_object.get_absolute_url())
