from django.shortcuts import render
from portfolio.models import Project, Item



# Create your views here.
def index(request):

    #on load, get all the item objects to be rendered
    items = Item.objects.all()
    context = {
        'items': items
    }
    
    return render(request, 'portfolio/index/index.html', context)


def project(request):

    #get the item clicked on
    item = request.GET.get("item",'')
    print(item)

    #pull the appropriate item obj from the database
    item_obj = Item.objects.get(reference = item)
    print(item_obj)
    #pull the project objs that contain the item object, and get related
    project_objs = Project.objects.filter(items = item_obj).prefetch_related()
    for p in project_objs:
        print(p.items.all())

    context = {
        'projects': project_objs,
        }

    return render(request, 'portfolio/partials/projects/projects.html', context)