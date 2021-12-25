from django.db.models.query import QuerySet
from django.http.response import ResponseHeaders
from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework import serializers
from rest_framework.serializers import Serializer
from .models import Stores
from .serializer import StoreSerializer
from django.shortcuts import get_object_or_404
from rest_framework.response import Response



class ItemsViewSet(viewsets.ModelViewSet):
    serializer_class=StoreSerializer
    queryset= Stores.objects.all()


    # To add a new item in the store
    def create(self,request):
        serializer=StoreSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Item added successfully!!'},status=status.HTTP_201_CREATED)
        return Response(Serializer.errors,status=status.HTTP_400_BAD_REQUEST)


    # To get the details of a particular product
    def retrieve(self, request, pk=None):
        queryset= Stores.objects.all()
        item = get_object_or_404(queryset, pk=pk)
        serializer = StoreSerializer(item)
        return Response(serializer.data)

    # To update details of a particular product in the store
    def update(self, request, pk):
        id=pk
        item=Stores.objects.get(pk=id)
        serializer=StoreSerializer(item,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"Data updated successfully!!"})
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    # To delete a item from the store
    def destroy(self,request,pk):
        id=pk
        item=Stores.objects.get(pk=id)
        item.delete()
        return Response({"message":"Item deleted successfully"})





