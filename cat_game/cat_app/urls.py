from django.contrib import admin
from django.urls import path

from cat_app.views.base import index_view
from cat_app.views.cat_info import cat_info_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_view),
    path('cat_info/', cat_info_view),
    path('warning/', index_view),
]
