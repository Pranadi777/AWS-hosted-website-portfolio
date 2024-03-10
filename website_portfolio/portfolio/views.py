from django.shortcuts import render
from portfolio.models import Project, Item



# Home page
def index(request):

    #on load, get all the item objects to be rendered
    items = Item.objects.all()
    context = {
        'items': items
    }
    
    return render(request, 'portfolio/index/index.html', context)

#pick a project to see
def project(request):

    #get the item clicked on
    item = request.GET.get("item",'')

    #pull the appropriate item obj from the database
    item_obj = Item.objects.get(reference = item)

    #pull the project objs that contain the item object, and get related
    project_objs = Project.objects.filter(items = item_obj).prefetch_related()

    context = {
        'projects': project_objs,
        }

    return render(request, 'portfolio/partials/projects/projects.html', context)


#show all projects
def all_projects(request):

    #get the item clicked on
    item = request.GET.get("item",'')

    #pull the project objs that contain the item object, and get related
    project_objs = Project.objects.all().prefetch_related()

    context = {
        'projects': project_objs,
        }

    return render(request, 'portfolio/all_projects/all_projects.html', context)

#Contact page
def contact(request):

    return render(request, 'portfolio/contact/contact.html')