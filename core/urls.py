from django.urls import path
from core.views import index 

urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'^$', index)
]
