from .models import DataApi
from .models import student
from rest_framework import serializers
from .models import emp

class GeeksModelSerializer(serializers.ModelSerializer):
    class Meta:
        model=DataApi
        
        fields=["id","name",'sal']
class studentModelSerializer(serializers.ModelSerializer):
    class Meta:
        model=student
        fields=['student_name','id','fee']
class empserializer(serializers.ModelSerializer):
    class Meta:
        model=emp
        fields=['empname','empid','sal']
    
