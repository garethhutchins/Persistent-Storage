from django.db import models

# Create your models here.
class persistent_storage(models.Model):
    name = models.TextField()
    file_name = models.TextField()
    model_type = models.TextField()
    num_topics = models.IntegerField()
    normalisation = models.TextField()

    def __str__(self):
        return self.name
