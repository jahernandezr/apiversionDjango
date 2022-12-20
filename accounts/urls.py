from django.urls import path
from . import views
from django.conf.urls.static import static

urlpatterns = [
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout"),
]
