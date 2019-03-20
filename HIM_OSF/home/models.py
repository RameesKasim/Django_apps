from django.db import models


class Request(models.Model):
    name = models.CharField(max_length=50)
    house = models.CharField(max_length=50)
    place = models.CharField(max_length=50)
    phone = models.BigIntegerField()
    type = models.CharField(max_length=50)
    help_needed = models.CharField(max_length=50)
    letter = models.CharField(max_length=100)
    approved_by = models.CharField(max_length=50)

    def get_names(self):
        return self.name

    def __str__(self):
        return self.name+' '+self.type+' '+self.help_needed+' '+self.approved_by
