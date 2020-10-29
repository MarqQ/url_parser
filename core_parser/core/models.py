from django.db import models


class MainUrl(models.Model):
    url = models.CharField(max_length=255)
    file = models.CharField(max_length=255)

    def __str__(self):
        return str(self.url)


class SecondaryUrl(models.Model):
    final_link = models.CharField(max_length=255, null=True)
    main_url = models.ForeignKey(MainUrl, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.final_link)
