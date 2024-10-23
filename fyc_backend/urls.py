from django.contrib import admin
from django.urls import path
import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("current-datetime", views.current_datetime),
]
