
from django.urls import path,include

from newapp import views

urlpatterns = [

    path('',views.new,name='new'),

  # path('add/',views.addition,name='addition'),
  #

]
