from django.shortcuts import render, redirect
from django.views.generic import View
from .models import Post
from .form import CommentsForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

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





