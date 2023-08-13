from django.db import models


class Cars(models.Model):
    CHOOSES = (('JEEP', 'JEEP'),
               ('SEDAN', 'SEDAN'),
               ('SUV', 'SUV'),
               ('MINIVAN', 'MINIVAN'),
               ('COUPE', 'COUPE'),
               ('WAGON', 'WAGON'),
               )

    category = models.CharField(max_length=15, null=False, blank=False, choices=CHOOSES)
    brand = models.CharField(max_length=25)
    model = models.CharField(max_length=25)
    power = models.PositiveIntegerField()
    image = models.ImageField(upload_to="cars",)
    description = models.TextField()
    price = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.id}/ {self.model}/ {self.brand}"

    def delete(self, *args, **kwargs):
        storage, path = self.image.storage, self.image.path
        super(Cars, self).delete(*args, **kwargs)
        storage.delete(path)


