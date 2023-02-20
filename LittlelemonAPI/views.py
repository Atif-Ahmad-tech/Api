from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, renderer_classes
from .models import Menuitem
from .serializer import menuitemSerializer
from django.shortcuts import get_object_or_404
###########   rensrers  ###############
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework_yaml.renderers import YAMLRenderer
from .models import catagory 
from .serializer import catagorySerializer
#############################
# Create your views here.
@api_view()
@renderer_classes([YAMLRenderer]) # <------ added 
def menu_items(request):
    items = Menuitem.objects.all()
    serialized_item = menuitemSerializer(items, many=True, context={'request': request})
    return Response(serialized_item.data)

@api_view()
def single_items(request, id):
    items = get_object_or_404(Menuitem, pk=id)
    serialized_item = menuitemSerializer(items)
    return Response(serialized_item.data)


##### added
@api_view() 
@renderer_classes ([TemplateHTMLRenderer])
def menu(request):
    items = Menuitem.objects.all()
    serialized_item = menuitemSerializer(items, many=True)
    return Response({'data':serialized_item.data}, template_name='menu-items.html')
     