Inventory

A REST service that can:

Add new products to the store
Update the status of the product
Can hard delete- remove the item from the store
Can soft delete- can change the status of the product if it's active or not
Can get the details of a particular product based on product id passed as a parameter in url

To add a new product- POST method

http://127.0.0.1:8000/api/store_management/add_item

 pass parameters-> {
    "Product_Name":"HideandSeek",
    "Product_Code":"HnS",
    "Quantity":5,
    "Type":"Bakery",
    "GST":2.90,
    "Price":50
}

To view the details of a product- GET method

http://127.0.0.1:8000/api/store_management/show_item/<pk>


To update any detail of a particular product in the store- PUT method

http://127.0.0.1:8000/api/store_management/update_item/<pk>

--> pass the data you want to update as the parameter. 


To soft delete product, that is, changing the active status to 0 from 1- Delete method

http://127.0.0.1:8000/api/store_management/soft_delete_item/<pk>


To hard delete product, that is, removing the product from the store- Delete method

http://127.0.0.1:8000/api/store_management/hard_delete_item/<pk>


