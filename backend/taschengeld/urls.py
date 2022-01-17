from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('taschengeldapp.urls')),
    path('admin/', admin.site.urls),
]

#Configure Admin Titles
admin.site.site_header = "Taschengeld App"
admin.site.site_title = "Taschengeld"

