from django.db import models
import uuid
from django.conf import settings
import os

# Create your models here.
class persistent_storage(models.Model):
    name = models.TextField(
     primary_key = True,
     default = uuid.uuid4,
     editable = False)
    file_name = models.TextField()
    model_type = models.TextField()
    num_topics = models.IntegerField()
    normalisation = models.TextField()
    save_model = models.FileField(upload_to='models',default='')

    def __str__(self):
        return self.name

    def delete(self, *args, **kwargs):
        filepath = str(self.save_model)
        os.remove(os.path.join(settings.MEDIA_ROOT, filepath))
        super().delete(*args, **kwargs)
