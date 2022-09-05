from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DeleteView, UpdateView
from commentapp.decorators import comment_ownership_required
from commentapp.forms import CommentCreationForm
from django.utils.decorators import method_decorator
from articleapp.models import Article
from commentapp.models import Comment
import json


# Create your views here.
class CommentCreateView(CreateView):
    model = Comment
    form_class = CommentCreationForm
    template_name = 'commentapp/create.html'

    def form_valid(self, form):
        temp_comment = form.save(commit=False) # article pk를 입력해주기 위해 commit=false
        temp_comment.article = Article.objects.get(pk=self.request.POST['article_pk'])
        temp_comment.writer = self.request.user
        parent_id = self.request.POST.get('parent_comment_id', None)
        temp_comment.parent_comment = Comment.objects.get(id=parent_id)
        temp_comment.save()
        
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('articleapp:detail', kwargs={'pk' : self.object.article.pk})


@method_decorator(comment_ownership_required, 'get')
@method_decorator(comment_ownership_required, 'post')
class CommentDeleteView(DeleteView):
    model = Comment
    context_object_name = 'target_comment'
    template_name = 'commentapp/delete.html'
    
    def get_success_url(self):
        return reverse('articleapp:detail', kwargs={'pk' : self.object.article.pk})


@method_decorator(comment_ownership_required, 'get')
@method_decorator(comment_ownership_required, 'post')
class CommentUpdateView(UpdateView):
    model = Comment
    context_object_name = 'target_comment'
    form_class = CommentCreationForm
    template_name = 'commentapp/update.html'

    def get_success_url(self):
        return reverse('articleapp:detail', kwargs={'pk' : self.object.article.pk})