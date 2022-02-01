from django.shortcuts import render
from django.urls import reverse_lazy
from .forms import *
from .models import *
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect
from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.edit import FormMixin
from datetime import datetime

# Create your views here.
from .utils import FormMixin


class NewsHome(ListView):
    model = HeadNews
    category = Category.objects.all()
    template_name = 'news/index.html'
    context_object_name = 'head_news'
    extra_context = {'title': 'Sports news', 'category': category, 'counter': 0}

    paginate_by = 4

    def get_queryset(self):
        return HeadNews.objects.filter(is_published=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['news'] = News.objects.all().filter(is_published=True)[:15]

        return context


class ShowArticle(DetailView, FormMixin):
    model = HeadNews
    template_name = 'news/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'show_news'
    category = Category.objects.all()
    extra_context = {'category': category}
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = context['show_news']
        context['news'] = News.objects.all().filter(is_published=True)[:15]
        context['comments'] = Comments.objects.filter(head_news=context['object']).select_related('user_name')
        context['form'] = AddCommentForm()

        return context

    def get_success_url(self):
        return reverse_lazy('article', kwargs={'post_slug': self.get_object().slug})

    def post(self, request, *args, **kwargs):
        form = AddCommentForm(request.POST)
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        try:
            self.object = form.save(commit=False)
            self.object.head_news = self.get_object()
            self.object.user_name = NewUser.objects.all().filter(username=self.request.user)[0]
            self.object.save()
        except Exception as es:
            print(es)
            print('_________________________')
        return super().form_valid(form)


class ShowPosts(DetailView, FormMixin):
    model = News
    template_name = 'news/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'show_news'
    category = Category.objects.all()
    extra_context = {'category': category}
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = context['show_news']
        context['news'] = News.objects.all().filter(is_published=True)[:15]
        context['comments'] = Comments.objects.filter(news=context['object']).select_related('user_name')
        context['form'] = AddCommentForm()

        return context

    def get_success_url(self):
        return reverse_lazy('news', kwargs={'post_slug': self.get_object().slug})

    def post(self, request, *args, **kwargs):
        form = AddCommentForm(request.POST)
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        try:
            self.object = form.save(commit=False)
            self.object.news = self.get_object()
            self.object.user_name = NewUser.objects.all().filter(username=self.request.user)[0]
            self.object.save()
        except Exception as es:
            print(es)
            print('_________________________')
        return super().form_valid(form)


class HeadNewsCategory(ListView):
    model = HeadNews
    category = Category.objects.all()
    template_name = 'news/index.html'
    context_object_name = 'head_news'
    extra_context = {'category': category}
    allow_empty = False
    paginate_by = 4
    x = ShowArticle()

    def get_queryset(self):
        return HeadNews.objects.filter(category__slug=self.kwargs['category_slug'], is_published=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = context['head_news'][0].category
        context['news'] = News.objects.all().filter(is_published=True)[:15]

        return context


class ShowHotNews(ListView):
    model = News
    template_name = 'news/post.html'
    category = Category.objects.all()
    context_object_name = 'hot_news'
    extra_context = {'title': 'Hot news', 'category': category}
    paginate_by = 30

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['news'] = News.objects.all().filter(is_published=True)[:15]
        return context

    def get_success_url(self):
        return reverse_lazy('article', kwargs={'post_slug': self.get_object().slug})


def del_comment_article(request, *args, **kwargs):
    comment = Comments.objects.get(id=kwargs['int'])
    comment.delete()
    print(kwargs)
    return HttpResponseRedirect('/article/' + kwargs['post_slug'])


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'news/registration.html'
    # form = RegisterUserForm()
    success_url = reverse_lazy('show_hot_news')
    category = Category.objects.all()
    extra_context = {'title': 'registration', 'category': category}

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['news'] = News.objects.all().filter(is_published=True)[:8]
        return context


class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'news/login.html'
    category = Category.objects.all()
    extra_context = {'title': 'login', 'category': category}

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['news'] = News.objects.all().filter(is_published=True)[:8]
        return context

    def get_success_url(self):
        return reverse_lazy('news_index')


class LogOutUser(LogoutView):
    pass

    def get_next_page(self):
        return reverse_lazy('news_index')


def del_comment_news(request, *args, **kwargs):
    comment = Comments.objects.get(id=kwargs['int'])
    comment.delete()
    print(kwargs)
    return HttpResponseRedirect('/news/' + kwargs['post_slug'])
