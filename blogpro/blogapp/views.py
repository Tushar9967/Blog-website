from django.shortcuts import get_object_or_404, render, redirect
from django.utils import timezone
from blogapp.forms import UserForm, NewPostForm, CommentForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from blogapp.models import NewPost, Comment
from django.views.generic import DetailView, ListView, UpdateView, DeleteView
from . import models
from django.urls import reverse_lazy
# Create your views here.


def index(request):
    newpost = NewPost.objects.all().order_by('-published_date')
    return render(request, 'blogapp/index.html', {"newpost": newpost})


def about(request):
    return render(request, 'blogapp/about.html')


def register(request):
    registered = False

    if request.method == "POST":
        user_form = UserForm(data=request.POST)

        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            registered = True

        else:
            print(user_form.errors)

    else:
        user_form = UserForm()

    return render(request, 'blogapp/registeration.html', {'user_form': user_form, 'registered': registered})


def user_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))

            else:
                return HttpResponse("Account not active")

        else:
            print("someone tried to login and failed!")
            print('username :{} ---- password : '.format(username, password))
            return HttpResponse('invalid login details supplied!')
    else:
        return render(request, 'blogapp/login.html', {})


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


# making new post page
def NewPostView(request):
    if request.method == "POST":
        form = NewPostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")

    else:
        form = NewPostForm()

    return render(request, 'blogapp/newpost.html', {'form': form})


# def DraftsView(request):
#     newpost=NewPost.objects.all()
#     return render(request,'blogapp/drafts.html',{'newpost':newpost})

# def DraftsEditView(request,id):
#     # newpost=NewPost.objects.get(id=id)
#     # return render(request,'blogapp/drafts_edit.html',{'newpost':newpost})
#     print("this from draft edit view")
#
#
#
#     context ={}
#
#     context["data"] = NewPost.objects.get(id = id)
#
#     return render(request, "blogapp/drafts_edit.html", context)

class DraftsView(ListView):
    context_object_name = 'newpost'
    model = models.NewPost

    # see newpost_list.html


class DraftsEditView(DetailView):
    context_object_name = 'draft_view'
    model = models.NewPost
    template_name = 'blogapp/newpost_detail.html'
    # pk_url_kwarg="id"


class DraftsUpdateView(UpdateView):
    fields = ('Author', 'Title', 'Text')
    model = models.NewPost


class DraftsDeleteView(DeleteView):
    print('This is from delete view')
    context_object_name = 'newpost'

    model = models.NewPost

    success_url = reverse_lazy("blogapp:drafts")

# def DraftsDeleteView(request, id):
#     # dictionary for initial data with
#     # field names as keys
#     context ={}
#
#     # fetch the object related to passed id
#     obj = get_object_or_404(NewPost, id = id)
#
#
#     if request.method =="POST":
#         # delete object
#         obj.delete()
#         # after deleting redirect to
#         # home page
#         return HttpResponseRedirect("blogapp/school_detail.html")
#
#     return render(request, "blogapp/newpost_confirm_delete.html", context)


def post_publish(request, pk):
    post = get_object_or_404(NewPost, pk=pk)
    # post = NewPost.objects.get()
    post.publish()
    return redirect('index')


def CommentView(request, pk):
    post = get_object_or_404(NewPost, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('blogapp:view_draft', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'blogapp/comment.html', {'form': form})


@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('blogapp:view_draft', pk=comment.post.pk)


@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.delete()
    return redirect('blogapp:view_draft', pk=comment.post.pk)
