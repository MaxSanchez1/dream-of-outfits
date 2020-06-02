from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    DeleteView,
)
from .forms import ArticleForm
from .models import Article


# def article_list_view(request):
#     queryset = Article.objects.all()
#     context = {
#         "object_list": queryset,
#     }
#     return render(request, "blog/article_list.html", context)


class ArticleListView(ListView):
    # if you wanted to use a different template than the one it found automatically,
    # you can use: template_name = 'whatever/whatever_list.html'
    queryset = Article.objects.all()


# def article_detail_view(request, title):
#     obj = get_object_or_404(Article, title=title)
#     context = {
#         "object": obj,
#     }
#     return render(request, "blog/article_detail.html", context)

class ArticleDetailView(DetailView):
    # if you wanted to use a different template than the one it found automatically,
    # you can use: template_name = 'whatever/whatever_list.html'
    # queryset = Article.objects.all()

    # this is how you override pk but what we want to do doesn't need it
    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Article, id=id_)


# def article_create_view(request):
#     form = ArticleForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         form = ArticleForm()
#     context = {
#         'form': form
#     }
#     return render(request, "blog/article_create.html", context)

# after you create a form, it uses that get_absolute_url method to take you to the post. You must have that
# configured properly or it will error out when you try and submit a form.
class ArticleCreateView(CreateView):
    template_name = 'blog/article_create.html'
    form_class = ArticleForm

    # doesn't have to go to the blog detail on success, can be overridden like so.
    # success_url = '/blog'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)


class ArticleUpdateView(UpdateView):
    template_name = 'blog/article_create.html'
    form_class = ArticleForm

    # remember, this doesn't have to be here, but we wanted to use id instead of pk so here it is
    # we need this method because we are getting a specific object to modify
    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Article, id=id_)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)


class ArticleDeleteView(DeleteView):
    template_name = 'blog/article_delete.html'

    # this is how you override pk
    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Article, id=id_)

    def get_success_url(self):
        return reverse('blog:article-list')


