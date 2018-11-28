#from django.contrib import admin
from django.urls import path
from resume import views

urlpatterns = [
    path(r'', views.list),
    #path(r'<int:id>',views.resume)
]
