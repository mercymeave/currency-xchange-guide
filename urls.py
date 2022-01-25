from django.contrib import admin
from django.urls import path, include
from converter import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('historical/', views.show_historical, name="historical"),
    path('live/', views.show_live, name="live")
]
