from rest_framework import serializers
from .models import Menuitem, catagory
from rest_framework.validators import UniqueValidator
 
# class menuitemSerializer(serializers.Serializer):
#     id= serializers.IntegerField()
#     title = serializers.CharField(max_length=255)
#     price = serializers.DecimalField(max_digits=6, decimal_places=2)
#     inventory = serializers.IntegerField()

class catagorySerializer(serializers.ModelSerializer):
    class Meta:
        model= catagory
        fields = ['id', 'title', 'slug']
    
# class menuitemSerializer(serializers.ModelSerializer):
#     catagory = catagorySerializer(read_only=True)
#     # def validate_price(self, value): ### <------  first method
#     #     if (value < 2):
#     #         raise serializers.ValidationError('Price should not be less than 2.0')
#     # def validate_inventory(self, value):
#     #     if (value < 0):
#     #         raise serializers.ValidationError('Stock cannot be negative')
    
#     def validate(self, attrs): ### <------  second method method
#         if(attrs['price']<2):
#             raise serializers.ValidationError('Price should not be less than 2.0')
#         if(attrs['inventory']<0):
#             raise serializers.ValidationError('Stock cannot be negative')
#         return super().validate(attrs)
#     class Meta:
#         model = Menuitem
#         fields = ['id', 'title', 'price', 'inventory','catagory']
#         extra_kwargs = {
#             'title': {
#                 'validators': [UniqueValidator(queryset=Menuitem.objects.all())]  ## unique title
#                 }
#             }
class MenuitemSerializer(serializers.ModelSerializer):
    catagory_id = serializers.IntegerField(write_only=True)
    catagory = catagorySerializer(read_only=True)
    class Meta:
        model = Menuitem
        fields = ['id','title','price','inventory','catagory','catagory_id']