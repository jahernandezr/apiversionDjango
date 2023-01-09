from django.urls import path
from . import views
from django.conf.urls.static import static

urlpatterns = [
    path('recobro/', views.getrecobros, name="recobro"),
    path('getnodocument/',views.getnodocument ,name="getnodocument"),
    path('insertrecobros/',views.insertrecobros ,name="insertrecobros"),
]
