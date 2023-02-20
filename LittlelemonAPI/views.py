from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, renderer_classes
from .models import Menuitem
from .serializer import menuitemSerializer
from django.shortcuts import get_object_or_404
##########################
from rest_framework.renderers import TemplateHTMLRenderer

#############################
# Create your views here.
@api_view()
def menu_items(request):
    items = Menuitem.objects.all()
    serialized_item = menuitemSerializer(items, many=True)
    return Response(serialized_item.data)

@api_view()
def single_items(request, id):
    items = get_object_or_404(Menuitem, pk=id)
    serialized_item = menuitemSerializer(items)
    return Response(serialized_item.data)


# @api_view() 
# @renderer_classes ([TemplateHTMLRenderer])
# def menu_items(request):
#     items = Menuitem.objects.all()
#     serialized_item = menuitemSerializer(items, many=True)
#     return Response({'data':serialized_item.data}, template_name='menu-items.html')
     