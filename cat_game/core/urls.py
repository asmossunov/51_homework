from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('cat_app.urls')),
    path('cat_info/', include('cat_app.urls')),
    path('warning/', include('cat_app.urls'))
]
