from django.db import models


class MainUrl(models.Model):
    url = models.CharField(max_length=255)
    file = models.CharField(max_length=255)

    def __str__(self):
        return str(self.url)
