from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from articleapp.models import Article

from searchapp.forms import SearchForm


# Create your views here.
class SearchFormView(FormView):
    form_class = SearchForm
    template_name = 'searchapp/search.html'

    def form_valid(self, form):
        word = form.cleaned_data['word']
        article_list = Article.objects.filter(Q(title__icontains=word) | Q(content__icontains=word)).distinct()

        context = {}
        context['article_list'] = article_list
        context['word'] = word
        return context
