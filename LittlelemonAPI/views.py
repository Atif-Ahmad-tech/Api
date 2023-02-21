from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, renderer_classes
from .models import Menuitem
from .serializer import menuitemSerializer
from django.shortcuts import get_object_or_404
###########   rensrers  ###############
from .models import catagory 
from .serializer import catagorySerializer
#############################
# Create your views here.
@api_view(['GET','POST'])
def menu_items(request):
    if (request.method=='GET'):
        items = Menuitem.objects.select_related('catagory').all()
        catagory_name = request.query_params.get('catagory')
        to_price = request.query_params.get('to_price')
        search = request.query_params.get('search')
        if catagory_name:
            items= items.filter(catagory__title=catagory_name)
        if to_price:
             items= items.filter(price__lte=to_price)
        if search:
            items= items.filter(title__startswith=search) ### startswith or contains or icontains(case INsensitive)
        serialized_item = menuitemSerializer(items, many=True, context={'request': request}) ## 
        return Response(serialized_item.data)
    if (request.method=='POST'):
        serialized_item = menuitemSerializer(data=request.data)
        serialized_item.is_valid(raise_exception=True)
        serialized_item.save()
        return Response(serialized_item.validated_data, status.HTTP_201_CREATED)
    
@api_view()
def single_items(request, id):
    items = get_object_or_404(Menuitem, pk=id)
    serialized_item = menuitemSerializer(items)
    return Response(serialized_item.data)



     