from django.urls import path
from Home_page.views import HomePage


urlpatterns = [
    path("", HomePage.as_view()),
]
