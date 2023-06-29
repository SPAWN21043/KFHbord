from django.shortcuts import render
from django.views import View
from Product_KFH.models import Category
from Home_page.models import InfoSite
from Cmd_services.commands import select_all_model


class CategoryPage(View):
    def get(self, request):
        info_site = select_all_model(Category)
        rere = select_all_model(InfoSite)

        return render(request, "index.html", {"infos": info_site})
# Create your views here.
