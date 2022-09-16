from django.http import HttpResponse, HttpResponseForbidden, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, RedirectView
from django.views.generic.list import MultipleObjectMixin
from accountapp.forms import AccountCreateForm, AccountUpdateForm
from accountapp.models import User
from accountapp.decorators import account_ownership_required
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
# from django.views.decorators.csrf import csrf_exempt
# from django.views.decorators.csrf import csrf_protect

from articleapp.models import Article

# Create your views here.
has_ownership = [account_ownership_required, login_required]

class AccountCreateView(CreateView):
    model = User
    form_class = AccountCreateForm
    success_url = reverse_lazy('profileapp:create')
    template_name = 'accountapp/create.html'


class AccountDetailView(DetailView, MultipleObjectMixin):
    model = User
    context_object_name = 'target_user'
    template_name = 'accountapp/detail.html'

    paginate_by = 10

    def get_context_data(self, **kwargs):
        object_list = Article.objects.filter(writer=self.get_object())
        return super(AccountDetailView, self).get_context_data(object_list=object_list, **kwargs)


@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class AccountUpdateView(UpdateView):
    model = User
    context_object_name = 'target_user'
    form_class = AccountUpdateForm
    success_url = reverse_lazy('home')
    template_name = 'accountapp/update.html'


@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class AccountDeleteView(DeleteView):
    model = User
    context_object_name = 'target_user'
    success_url = reverse_lazy('accountapp:login')
    template_name = 'accountapp/delete.html'


class AccountFollowView(RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        return reverse('accountapp:detail', kwargs={'pk' : self.request.GET.get('user_pk')})

    def get(self, request, *args, **kwargs):
        
        user = get_object_or_404(User, pk=self.request.GET.get('user_pk'))

        if user != self.request.user:
            if user.followers.filter(pk=self.request.user.pk).exists():
                user.followers.remove(self.request.user)
            else:
                user.followers.add(self.request.user)

        return super(AccountFollowView, self).get(request, *args, **kwargs)