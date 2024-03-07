from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    #debug toolbar
    path("__debug__/", include("debug_toolbar.urls")),
]

htmx_urlpatterns = [
    path('project/', views.project, name='project'),
]

urlpatterns += htmx_urlpatterns