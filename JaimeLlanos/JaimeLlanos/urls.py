
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api_jaimellanos/', include('api_jaimellanos.urls'))


]
