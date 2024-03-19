from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('all_projects/', views.all_projects, name='all_projects'),
    path('all_publications/', views.all_publications, name='all_publications'),
    path('skills/', views.skills, name='skills'),
    path('hobbies/', views.hobbies, name='hobbies'),
    path('contact/', views.contact, name='contact'),
    #debug toolbar
    path("__debug__/", include("debug_toolbar.urls")),
]

htmx_urlpatterns = [
    path('project/', views.project, name='project'),
]

urlpatterns += htmx_urlpatterns