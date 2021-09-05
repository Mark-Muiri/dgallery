from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name = ''),    
     path('search/', views.search_results, name = 'search_results')
]