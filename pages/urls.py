from django.urls import path
from . import views

urlpatterns = [
    path("index",views.index ,name="index"),
    path("about",views.about ,name="about"),
    path("addForm",views.addForm ,name="addForm"),
    path("loginForm",views.lform ,name="loginForm")
]

#http://localhost:8000/pages/
#http://localhost:8000/pages/privace
#ii=http://localhost:8000/pages/index
#aa=http://localhost:8000/pages/about
