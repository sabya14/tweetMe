from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Tweet
from .forms import TweetModelForm
from .mixins import FormUserNeededMixins,UserOwnerMixins
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.urls import reverse_lazy


class TweetCreateView(FormUserNeededMixins, LoginRequiredMixin, CreateView):
    form_class = TweetModelForm
    template_name = 'tweets/tweet_create.html'
    # success_url = reverse_lazy('tweet:list')


class TweetUpdateView(LoginRequiredMixin, UserOwnerMixins, UpdateView):
    queryset = Tweet.objects.all()
    form_class = TweetModelForm
    template_name = 'tweets/update_view.html'



class TweetDetailView(DetailView):
    queryset = Tweet.objects.all()

    # def get_object(self, queryset=queryset):
    #     pk = self.kwargs.get('id')
    #     return Tweet.objects.get(id=pk)


class TweetListView(ListView):

    def get_queryset(self,*args,**kwargs):
        qs = Tweet.objects.all()
        query = self.request.GET.get('q',None)
        print(query)
        if query is not None:
            qs = qs.filter(Q(content__icontains=query) |
                           Q(user__username__icontains=query))
            # qs = Tweet.objects.get(id=query)
            # return HttpResponseRedirect(q.get_absolute_url())
        return qs

    def get_context_data(self, **kwargs):
        context = super(TweetListView,self).get_context_data(**kwargs)
        context['create_form'] = TweetModelForm()
        context['create_url'] = reverse_lazy('tweet:create')
        return context

class TweetDeleteView(LoginRequiredMixin, UserOwnerMixins, DeleteView):
    queryset = Tweet.objects.all()
    form_class = TweetModelForm
    template_name = 'tweets/confirm_delete.html'
    success_url = '/tweets/'


def tweet_detail_view(request):
    object = Tweet.objects.get(id=id)
    return render(request, 'tweets/detail_view.html', {"content": object})


def tweet_list_view(request, ):
    queryset = Tweet.objects.all()
    context = {
        "object_list": queryset
    }
    print(context)
    return render(request, 'tweets/list_view.html', context)
