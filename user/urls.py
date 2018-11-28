from django.contrib import admin
from django.urls import path
from user import views


app_name="users"

urlpatterns = [
    path(r'',views.list,name="list"),
    #path(r'',views.UserListView.as_view(),name="list"),
    path(r'<int:id>',views.update, name="read"),
    path(r'<int:id>/update',views.update, name="update"),
    path(r'<int:id>/delete',views.delete,name="delete"),
    path(r'create',views.create,name="create")

]
