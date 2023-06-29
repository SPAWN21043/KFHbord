from django.db.models import Q
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from Home_page.models import InfoSite
from Product_KFH.models import Category
from Cmd_services.commands import select_all_model, category_filter


# Create your views here.
class HomePage(ListView):
    model = InfoSite
    template_name = 'index.html'
    context_object_name = 'infos'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cat_len = len(select_all_model(Category))
        if cat_len > 2:
            category_all = select_all_model(Category)
            context['all_cat'] = category_all
            context['cat1'] = category_all[0]
            context['cat2'] = category_all[1]
            context['rest_category'] = category_filter(Category, category_all[0].id, category_all[1].id)
            print(context)
        elif cat_len == 2:
            category_all = select_all_model(Category)
            context['all_cat'] = category_all
            context['cat1'] = category_all[0]
            context['cat2'] = category_all[1]
            context['rest_category'] = []
            print(context)
        else:
            category_all = select_all_model(Category)
            context['all_cat'] = category_all
            context['cat1'] = category_all[0]
            context['cat2'] = category_all[0]
            context['rest_category'] = []
            print(context)
        return context
