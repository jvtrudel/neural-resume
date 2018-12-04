from django.urls import path
from resume import views


app_name='resumes'

urlpatterns = [
    path(r'',views.list, name='list'),
    path(r'<int:id>',views.show, name='show'),
    path(r'create',views.create,name='create'),
    path(r'update/<int:id>',views.update,name='update'),
    path(r'delete/<int:id>',views.delete,name='delete')
]
