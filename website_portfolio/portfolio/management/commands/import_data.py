from django.core.management.base import BaseCommand
from portfolio.models import Project, Item, Link
from portfolio.data.project_data import projects, items, links

class Command(BaseCommand):
    help = 'Creates import data for projects and items'

    def handle(self, *args, **options):

        Item.objects.all().delete()
        Link.objects.all().delete()
        Project.objects.all().delete()

        for item in items:

            Item.objects.get_or_create(
                custom_id = item['custom_id'],
                name = item['name'],
                reference = item['reference'],
                type = item['type'],
                image = item['image'],
            )
        for link in links:
            Link.objects.get_or_create(
                custom_id = link['custom_id'],
                name = link['name'],
                description = link['description'],
                url = link['url'],
            )

        for project in projects:

            project_obj, created = Project.objects.get_or_create(
                custom_id = project['custom_id'],
                title = project['title'],
                goal = project['goal'],
                method = project['method'],
                result = project['result'],
                image = project['image']
            )
            #creates the ManyToMany relationship based on the custom_id field
            project_obj.items.set(Item.objects.filter(custom_id__in = project['items']))
            project_obj.links.set(Link.objects.filter(custom_id__in = project['links']))

        print("succesfully reset data")