from django.http import response, JsonResponse
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from store_management.serializer import StoreSerializer
from django.db import transaction
from store_management.models import Stores
from django.shortcuts import get_object_or_404 
from django.core.exceptions import ObjectDoesNotExist, ValidationError
from django.db import IntegrityError
from inventory.utils.exceptionhandler import CustomAPIException 
from django.forms.models import model_to_dict
from rest_framework import status, viewsets

# To create new entry in the store
class InsertItemsView(APIView):
    @transaction.atomic
    def post(self, request,code= None, *args, **kwargs):
        try:
            if not code:    
                data=request.data
                store=Stores()
                store.name= data.get('Product_Name')
                store.code= data.get('Product_Code')
                store.active= 1
                store.quantity= data.get('Quantity')
                store.type=data.get('Type')
                store.gst=data.get('GST')
                store.price=data.get('Price')
                store.save()
                return Response({"Success": True, "message": "Item added successfully!!", "status_code": 200 })
        except IntegrityError as e:
            return Response({"message": "This entry is already present or enter the right credentials"})
        
#To view the details of a product
class ShowItemsView(APIView):
    @transaction.atomic
    def get(self,request, pk=None):
        #Method-1 (Using serializer)
        # try:
        #     if pk:
        #         i=Stores.objects.get(pk=pk)
        #         serializer= StoreSerializer(i)
        #         return Response({"Success": True, "message": "This item was requested!!","data":serializer.data, "status_code": 200 })
        #     # i=Stores.objects.all()
        #     # serializer= StoreSerializer(i, many= True)
        #     # return Response({"Success": True, "message": "All items!!","data":serializer.data,  "status_code": 200 })
        # except:
        #     return Response({"message":"This object does not exist"}, status_code=status.HTTP_404_NOT_FOUND)
        #Method-2 (Using model_to_dict)
        try:
            if pk:
                i=Stores.objects.get(pk=pk)
                j=model_to_dict(i)
                return Response({"Success": True, "message": "This item was requested!!","data":j  })
            # i=Stores.objects.all()
            # serializer= StoreSerializer(i, many= True)
            # return Response({"Success": True, "message": "All items!!","data":serializer.data,  "status_code": 200 })
        except:
            raise CustomAPIException("This object does not exist", status_code=status.HTTP_404_NOT_FOUND)

# To delete a product from the store
class DeleteItemsView(APIView):
    @transaction.atomic
    def delete(self, request, pk=None):
        try:
            if pk:
                i= Stores.objects.get(pk=pk)
                i.delete()
                return Response({"message": "Item is successfully deleted!!"})
        except:
            raise CustomAPIException("This object does not exist", status_code=status.HTTP_404_NOT_FOUND)

#To make a product as not active
class SoftDeleteItemsView(APIView):
    @transaction.atomic
    def delete(self, request, pk=None):
        try:
            if pk:
                store= Stores.objects.get(pk=pk)
                store.active=0
                store.save()
                return Response({"message": "Soft deleted!!"})
        except:
            raise CustomAPIException("This object does not exist", status_code=status.HTTP_404_NOT_FOUND)

#To update the details of a product
class UpdateItemsView(APIView):
    @transaction.atomic
    def put(self, request, pk=None, *args, **kwargs):
        try:
            if pk:
                store= Stores.objects.get(pk=pk)
                serializer=StoreSerializer(store, data=request.data, partial= True)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data)
                return Response(serializer.errors)
        except:
            raise CustomAPIException("This object does not exist", status_code=status.HTTP_404_NOT_FOUND)









