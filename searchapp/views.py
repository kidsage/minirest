from django.views.generic import ListView
from django.db.models import Q

from articleapp.models import Article


# Create your views here.
class SearchFormView(ListView):
    model = Article
    template_name = 'searchapp/search.html'
    context_object_name = 'search_list'
    paginate_by = 20

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = self.model.objects.all()
        
        if query:
            object_list = object_list.filter(
                Q(title__icontains=query) | Q(content__icontains=query)
            )

        context = {}
        context['object_list'] = object_list
        context['query'] = query

        return context
