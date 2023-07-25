from django.db import models


class Bikes(models.Model):

    CHOOSES = (('TURER', 'TURER'),
               ('CROSS', 'CROSS'),
               )

    category = models.CharField(max_length=15, null=False, blank=False, choices=CHOOSES)
    brand = models.CharField(max_length=25)
    model = models.CharField(max_length=25)
    image = models.ImageField(upload_to="motorbikes_images",)
    description = models.TextField()
    price = models.IntegerField()

    def __str__(self):
        return f"{self.id}/ {self.model}/ {self.brand}"

    def delete(self, *args, **kwargs):
        storage, path = self.image.storage, self.image.path
        super(Bikes, self).delete(*args, **kwargs)
        storage.delete(path)
