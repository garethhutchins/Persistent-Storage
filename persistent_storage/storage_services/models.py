from django.db import models
import uuid
from django.conf import settings
import os
from django.db.models import JSONField
#Run these after making a change
#python manage.py makemigrations
#python manage.py migrate

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
    topic_labels = JSONField(default=list, blank=True, null=True)
    save_model = models.FileField(upload_to='models',default='')
    topics_image = models.FileField(upload_to='models',default='')

    def __str__(self):
        return self.name

    def delete(self, *args, **kwargs):
        #Delete the files
        filepath = str(self.save_model)
        os.remove(os.path.join(settings.MEDIA_ROOT, filepath))
        imagefile = str(self.topics_image)
        os.remove(os.path.join(settings.MEDIA_ROOT, imagefile))
        super().delete(*args, **kwargs)
    
    def save(self, *args, **kwargs):
        try:
            this = persistent_storage.objects.get(name=self.name)
            if this.save_model != self.save_model:
                filepath = str(this.save_model)
                os.remove(os.path.join(settings.MEDIA_ROOT, filepath))
            if this.topics_image != self.topics_image:
                imagefile = str(this.topics_image)
                os.remove(os.path.join(settings.MEDIA_ROOT, imagefile))
        except: pass
        super(persistent_storage, self).save(*args, **kwargs)
