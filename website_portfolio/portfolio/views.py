from django.shortcuts import render
from portfolio.models import Project, Item



# Create your views here.
def index(request):

    #on load, get all the objects you need to render
    languages = Item.objects.filter(type = 'language')
    awss = Item.objects.filter(type = 'aws')
    frameworks = Item.objects.filter(type = 'framework')


    context = {
        'languages':languages,
        'awss': awss,
        'frameworks': frameworks
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
    project_objs = Project.objects.filter(items = item_obj).prefetch_related("items")
    print(project_objs)



    context = {
        'projects': project_objs,
        }

    return render(request, 'portfolio/partials/projects/projects.html', context)