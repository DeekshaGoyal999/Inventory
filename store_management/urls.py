from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

#Creating router object
router=DefaultRouter()

# Register ItemsViewSet with router
router.register('stores',viewset=views.ItemsViewSet, basename='Items')

#The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),

]