from rest_framework.serializers import ModelSerializer
from rest_framework import  serializers
from .models import Note


class NoteSerializer(serializers.ModelSerializer):
    owner=serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Note

        fields = ['id','owner','title','content','created_at', 'owner','updated_at','file']
        read_only_fields =['created_at','updated_at','owner']