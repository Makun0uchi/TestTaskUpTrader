from django.urls import path
from . import views


urlpatterns = [
    path('<path:slug>/', views.menu_view),
    path('', views.menu_view),
]
