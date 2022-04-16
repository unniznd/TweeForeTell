
from django.contrib import admin
from django.urls import path

from predictor import views as predictor_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',predictor_views.home),
    path('home/',predictor_views.home)
]
