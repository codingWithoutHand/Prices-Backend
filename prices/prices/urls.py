from django.urls import include,path
from django.contrib import admin

urlpatterns = [
    path('home/', include('home.urls')),
    path('admin/', admin.site.urls),
]
