from rest_framework import serializers
from .models import persistent_storage

class StorageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = persistent_storage
        fields = ('name','file_name','model_type','num_topics','normalisation','topic_labels','save_model')