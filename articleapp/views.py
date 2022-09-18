from django import views
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, ListView, RedirectView, TemplateView
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from articleapp.decorators import article_ownership_required
from django.views.generic.edit import FormMixin

from articleapp.forms import ArticleCreationForm
from articleapp.models import Article, Like
from projectapp.models import Project
from commentapp.models import Comment
from commentapp.forms import CommentCreationForm

import json

# Create your views here.
@method_decorator(login_required, 'get')
@method_decorator(login_required, 'post')
class ArticleCreateView(CreateView):
    model = Article
    form_class = ArticleCreationForm
    template_name = 'articleapp/create.html'

    def form_valid(self, form):
        temp_article = form.save(commit=False)
        temp_article.writer = self.request.user
        temp_article.save()
        form.save_m2m() #
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('articleapp:detail', kwargs={'pk' : self.object.pk})


class ArticleDetailView(FormMixin, DetailView):
    model = Article
    form_class = CommentCreationForm
    context_object_name = 'target_article'
    template_name = 'articleapp/detail.html'


@method_decorator(article_ownership_required, 'get')
@method_decorator(article_ownership_required, 'post')
class ArticleUpdateView(UpdateView):
    model = Article
    context_object_name = 'target_article'
    form_class = ArticleCreationForm
    template_name = 'articleapp/update.html'

    def get_success_url(self):
        return reverse('articleapp:detail', kwargs={'pk' : self.object.pk})


@method_decorator(article_ownership_required, 'get')
@method_decorator(article_ownership_required, 'post')
class ArticleDeleteView(DeleteView):
    model = Article
    context_object_name = 'target_article'
    success_url = reverse_lazy('articleapp:list')
    template_name = 'articleapp/delete.html'
    

# 여러개의 object를 보여줄 수 있는 게시판 형식의 뷰 > list view
# pagination(페이지화) > 넘버링 이용해서 페이지 바꿀 수 있는. (무한 스크롤이랑은 다름)
class ArticleListView(ListView):
    model = Article
    context_object_name = 'article_list'
    template_name = 'articleapp/list.html'
    # paginate_by = 20

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['project_list'] = Project.objects.all()
        return context

@method_decorator(login_required, 'get')
class ArticleLikesView(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        return reverse('articleapp:detail', kwargs={'pk': kwargs['pk']})

    def get(self, request, *args, **kwargs):
        user = self.request.user
        article = get_object_or_404(Article, pk=kwargs['pk'])

        if Like.objects.filter(user=user, article=article).exists():
            article.liked_user.remove()
            Like.objects.filter(user=user, article=article).delete()
            messages.add_message(self.request, messages.ERROR, '좋아요가 취소되었습니다.')
            return HttpResponseRedirect(reverse('articleapp:detail', kwargs={'pk':kwargs['pk']}))
        else:
            article.liked_user.add()
            Like(user=user, article=article).save()
            messages.add_message(self.request, messages.SUCCESS, '좋아요가 반영되었습니다.')
            # return HttpResponseRedirect(reverse('articleapp:detail', kwargs={'pk':kwargs['pk']}))

        return super(ArticleLikesView, self).get(self.request, *args, **kwargs)


class TagCloudView(TemplateView):
    template_name = 'articleapp/taggit/cloud.html'


class TaggedObjectView(ListView):
    model = Article
    template_name = 'articleapp/taggit/list.html'
    
    def get_queryset(self):
        return Article.objects.filter(tags_name=self.kwargs.get('tag'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tagname'] = self.kwargs['tag']
        return context