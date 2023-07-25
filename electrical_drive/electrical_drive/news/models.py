import datetime

from django.db import models


class Allnews(models.Model):

    category = models.CharField(max_length=15, null=False, blank=False)
    image = models.ImageField(upload_to="news_images",)
    description = models.TextField()
    data = models.DateTimeField(default=datetime.datetime.now)


    def __str__(self):
        return f"{self.id}/ {self.category}/ {self.data}"

    def delete(self, *args, **kwargs):
        storage, path = self.image.storage, self.image.path
        super(Allnews, self).delete(*args, **kwargs)
        storage.delete(path)
