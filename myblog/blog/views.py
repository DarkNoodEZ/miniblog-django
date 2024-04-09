from django.shortcuts import render, redirect
from django.views.generic import View
from .models import Post
from .form import CommentsForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from .models import Post
from django.shortcuts import redirect
from django.views import View
from django.shortcuts import render


class PostListView(View):
    #Вывод записей
    paginate_by = 2
    def get(self, request):
        posts = Post.objects.all()  # fetching all post objects from database
        p = Paginator(posts, 2)  # creating a paginator object
        # getting the desired page number from url
        page_number = request.GET.get('page')
        try:
            page_obj = p.get_page(page_number)  # returns the desired page object
        except PageNotAnInteger:
            # if page_number is not an integer then assign the first page
            page_obj = p.page(1)
        except EmptyPage:
            # if page is empty then return last page
            page_obj = p.page(p.num_pages)
        context = {'page_obj': page_obj}
        # sending the page object to index.html
        return render(request, 'blog/blog.html', context)

class PostDetail(View):
    '''отдельная страница записи'''
    def get(self, request, pk):
        post = Post.objects.get(id=pk)
        return render(request, 'blog/blog_detail.html', {'post': post})


class AddComments(View):
    '''добавление комментариев'''

    def post(self, request, pk):
        form = CommentsForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.post_id = pk
            form.save()
        return redirect(f'/{pk}')

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Validate form data
        if not username or not email or not password:
            return render(request, 'register.html', {'error': 'Please fill in all fields'})

        # Ensure password is properly hashed
        user = User.objects.create_user(username=username, email=email)
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('/')  # Перенаправление на административную панель
    return render(request, 'register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('/')  # Перенаправление на административную панель
    return render(request, 'login.html')


def logout(request):
    auth_logout(request)
    return redirect('/')





