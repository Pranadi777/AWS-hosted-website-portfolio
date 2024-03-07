from django.db import models

class Item(models.Model):
    custom_id = models.IntegerField(unique=True)
    name = models.CharField(max_length = 20)
    reference = models.CharField(max_length = 20, null=True)
    type = models.CharField(max_length = 20, null=True)

    class Meta:
        ordering = ['custom_id']
    
    def __str__(self):
        return self.name

class Project(models.Model):
    custom_id = models.IntegerField(unique=True)
    title = models.CharField(max_length = 50)
    goal = models.CharField(max_length = 200)
    method = models.CharField(max_length = 500)
    result = models.CharField(max_length = 500)
    items = models.ManyToManyField(Item, symmetrical=False, blank=True)
    image = models.CharField(max_length = 50)

    class Meta:
        ordering = ['custom_id']
    
    def __str__(self):
        return self.title

