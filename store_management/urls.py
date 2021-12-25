from django.urls import path
from . import views


urlpatterns = [
    path('add_item', views.InsertItemsView.as_view(),name='create item' ),
    # path('show_item', views.ShowItemsView.as_view(),name='show all item' ),
    path('show_item/<int:pk>', views.ShowItemsView.as_view(),name='show item' ),
    path('hard_delete_item/<int:pk>', views.DeleteItemsView.as_view(),name='delete item' ),
    path('soft_delete_item/<int:pk>', views.SoftDeleteItemsView.as_view(),name='soft delete item' ),
    path('update_item/<int:pk>', views.UpdateItemsView.as_view(),name='update item' ),
]
