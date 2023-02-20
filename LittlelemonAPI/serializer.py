from rest_framework import serializers
from .models import Menuitem, catagory

 
# class menuitemSerializer(serializers.Serializer):
#     id= serializers.IntegerField()
#     title = serializers.CharField(max_length=255)
#     price = serializers.DecimalField(max_digits=6, decimal_places=2)
#     inventory = serializers.IntegerField()

class catagorySerializer(serializers.ModelSerializer):
    class Meta:
        model= catagory
        fields = ['id', 'title', 'slug']
    
class menuitemSerializer(serializers.ModelSerializer):
    catagory = catagorySerializer()
    class Meta:
        model = Menuitem
        fields = ['id', 'title', 'price', 'inventory','catagory']
        