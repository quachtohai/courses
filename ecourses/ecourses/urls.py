
from django.contrib import admin
from django.urls import path, include, re_path
from courses.admin import admin_site

urlpatterns = [
    path('admin/', admin_site.urls),
    path('', include('courses.urls')),
    re_path(r'^ckeditor/', include('ckeditor_uploader.urls')),
]
