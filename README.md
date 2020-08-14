# Inventory-Manager
This is a small personal sideproject of mine.

The app consists of two parts, a web client and a server. 

## Web client
This module is a react based web client.
It will be served by the server.
The communication between client/server will be thru the servers /api route.

## Server
This server will store items in a inventory manager.
It will simulate a warehouse-like structure of items and shelfs/boxes.
MongoDB will be utilized as the storage medium.
Primary language of the server is Python(Flask).

## /api
### Add Category 
For adding a new category, perform a post request on /api/new_category
where the data is labeld as follows
name : "name"
desctiption : "desc"

### Add item
For adding a new item, perform a post request on /api/new_item
where the data is labeld as follows
name : "name"
categoryID : "category_id"

### Viewing items
For viewing items, do a get request on /api/get_items.
For a specific category_id do /api/get_items/category_id, where category_id is substituted for the id
