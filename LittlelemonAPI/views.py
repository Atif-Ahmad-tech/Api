from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, renderer_classes, permission_classes
from .models import Menuitem
from .serializer import menuitemSerializer
from django.shortcuts import get_object_or_404
##########################
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import TemplateHTMLRenderer
from .models import catagory 
from .serializer import catagorySerializer
#############################
# Create your views here.
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
#     return Response({'data':serialized_item.data}, template_name='index.html', )

@api_view()
@permission_classes([IsAuthenticated])
def secret(request):
    return Response({'message':'some secret messsage '})       

@api_view()
@permission_classes([IsAuthenticated])
def manager_view(request):
    if request.user.groups.filter(name='manager').exists():
        return Response({'message':'only manager should see this'})
    else:
        return Response({'message':'you are not authorized'}, 403)



     