from django.urls import path
from . import views

app_name = "movies"
urlpatterns = [
    path('', views.home, name="home"),
    path('movie/<pk>', views.playvideo, name="play"),
    path('film/<pk>', views.playlongvideo , name="longvideo"),
    path('comment/<pk>', views.comment, name="comment"),
    path('all/movies', views.show_all, name="all"),
    path('search', views.search, name="search"),
    path('', views.error_404, name="handler404"),
    path('', views.error_500, name="handler505"),
]
