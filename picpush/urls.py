from django.urls import path
from . import views

urlpatterns=[
    path('',views.welcome,name = 'welcome'),
    path('today/',views.pics_of_day,name='picsToday'),
    path('archives/<pic_id>/',views.past_days_pics,name='pastPics')
]