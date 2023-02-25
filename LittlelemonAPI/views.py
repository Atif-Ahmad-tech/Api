from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.decorators import api_view, renderer_classes
from .models import Menuitem
from .serializer import MenuitemSerializer
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator, EmptyPage ##### added to this branch (pagination)
###########   rensrers  ###############
from .models import catagory 
from .serializer import catagorySerializer
#############################
# Create your views here.
# @api_view(['GET','POST'])
# def menu_items(request):
#     if (request.method=='GET'):
#         items = Menuitem.objects.select_related('catagory').all()
#         catagory_name = request.query_params.get('catagory')
#         to_price = request.query_params.get('to_price')
#         search = request.query_params.get('search')
#         perpage = request.query_params.get('perpage', default=2)   ##### added to this branch (pagination)
#         page = request.query_params.get('page', default=1)          ##### added to this branch (pagination)
#         if catagory_name:
#             items= items.filter(catagory__title=catagory_name)
#         if to_price:
#              items= items.filter(price__lte=to_price)
#         if search:
#             items= items.filter(title__startswith=search) ### startswith or contains or icontains(case INsensitive)
#         paginator = Paginator(items, per_page=perpage)
#         try:                                 ##### added to this branch (pagination)
#             items = paginator.page(page)      ##### added to this branch (pagination)
#         except EmptyPage:                        ##### added to this branch (pagination)
#             []
#         serialized_item = menuitemSerializer(items, many=True, context={'request': request}) ## 
#         return Response(serialized_item.data)
#     if (request.method=='POST'):
#         serialized_item = menuitemSerializer(data=request.data)
#         serialized_item.is_valid(raise_exception=True)
#         serialized_item.save()
#         return Response(serialized_item.data, status.HTTP_201_CREATED)
    
# @api_view()
# def single_items(request, id):
#     items = get_object_or_404(Menuitem, pk=id)
#     serialized_item = menuitemSerializer(items)
#     return Response(serialized_item.data)



class CatagoriesView(generics.ListCreateAPIView):
    queryset = catagory.objects.all()
    serializer_class = catagorySerializer

class MenuItemsView(generics.ListCreateAPIView):
    queryset = Menuitem.objects.all()
    serializer_class = MenuitemSerializer
    ordering_fields = ['price', 'inventory']
    filterset_fields = ['price', 'inventory']
    search_fields = ['title']
