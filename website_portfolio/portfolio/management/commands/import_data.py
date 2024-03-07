from django.core.management.base import BaseCommand
from portfolio.models import Project, Item
from portfolio.data.project_data import projects, items

class Command(BaseCommand):
    help = 'Creates import data for projects and items'

    def handle(self, *args, **options):

        Item.objects.all().delete()
        Project.objects.all().delete()

        for item in items:

            Item.objects.get_or_create(
                custom_id = item['custom_id'],
                name = item['name'],
                reference = item['reference'],
                type = item['type'],
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

            project_obj.items.set(Item.objects.filter(custom_id__in = project['items']))

        print("succesfully reset data")