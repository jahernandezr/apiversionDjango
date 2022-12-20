from django.urls import path
from . import views
from django.conf.urls.static  import static

urlpatterns = [
    path('inventario/', views.viewinventario, name="inventario"),
    path('insertinventario/', views.insertinventario, name="insertinventario"),
    path('buscarnit/',views.buscarnit, name="buscarnit"),
    path('buscarnitall/',views.buscarnitall, name="buscarnitall"),
    path('buscarmodulos/', views.buscarmodulos, name="buscarmodulos"),
]
