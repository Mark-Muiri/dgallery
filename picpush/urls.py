from django.urls import path
from . import views

urlpatterns=[
    path('',views.welcome,name = 'welcome'),
    path('today/',views.pics_of_day,name='picsToday')
]