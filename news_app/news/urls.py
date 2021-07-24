from django.conf.urls import url
from django.urls import path
from .views import *


urlpatterns = [
    path('api/news', news_list),
    path('api/search', ListFilter.as_view())
]