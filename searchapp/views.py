from django.views.generic import ListView
from django.db.models import Q
from articleapp.models import Article


# Create your views here.
class SearchListView(ListView):
    model = Article
    template_name = 'searchapp/search.html'
    context_object_name = 'search_list'
    paginate_by = 20
    paginate_orphans = 5

    def get_context_data(self, **kwargs):
        context = super(SearchListView, self).get_context_data()
        
        page = context['page_obj']
        paginator = page.paginator
        pagelist = paginator.get_elided_page_range(page.number, on_each_side=3, on_ends=0)
        
        query = self.request.GET.get('q')
        object_list = self.model.objects.all()
        
        if query:
            object_list = object_list.filter(
                Q(title__icontains=query) | Q(content__icontains=query)
            )

        context['pagelist'] = pagelist
        context['word'] = query
        context['object_list'] = object_list

        return context