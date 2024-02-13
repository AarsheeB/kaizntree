# Install prerequisites-
1. Install pip and django using the following
   `pip install django`
2. Create your project
   `django-admin startproject yourprojectname`
3. Go to the project path
    `cd yourprojectname `
4. Create a django app
   `python manage.py startapp inventory_app`
5. Install Django REST framework
   `pip install djangorestframework`
6. Then create folders in your app using
   `touch foldername`

# Run the code-
1. Run the code with following commands-
   `python manage.py makemigrations`
   `python manage.py migrate`
2. Create a Django admin-
   `python manage.py createsuperuser`
3. Run the development server-
   `python manage.py runserver`
4. Access the django admin using the following url-
   [Link Text](http://127.0.0.1:8000/admin/)

# Run the login page in React-
1. Download frontend.zip
2. Go to src
3. Run npm start

# For the backend-
1. Download the ItemDashboard.zip
2. Use the following commands
3. `python manage.py makemigrations`
4. `python manage.py migrate`
5.  `python manage.py runserver`
6.  Use the API endpoints given below in postman-
   - Endpoint: GET /api/items/
      - Description: Retrieve a list of all items with details such as SKU, name, category, tags, stock status, and available stock.

   - Retrieve Single Item:
      - Endpoint: GET /api/items/{item_id}/
      - Description: Retrieve details for a specific item identified by its item_id.

   - Create New Item:
      - Endpoint: POST /api/items/
      - Description: Create a new item by providing necessary details in the request body.

   - Update Item:
      - Endpoint: PUT /api/items/{item_id}/
      - Description: Update details of a specific item identified by its item_id.

   - Delete Item:
      - Endpoint: DELETE /api/items/{item_id}/
      - Description: Delete a specific item identified by its item_id.

   - Filter Items by Category:
      - Endpoint: GET /api/items/?category={category_id}
      - Description: Retrieve a list of items filtered by a specific category identified by category_id.

   - Filter Items by Stock Status:
      - Endpoint: GET /api/items/?stock_status={status}
      - Description: Retrieve a list of items filtered by stock status (e.g., in stock, out of stock).

   - Filter Items by Date Range:
      - Endpoint: GET /api/items/?start_date={start_date}&end_date={end_date}
      - Description: Retrieve items created within a specified date range.

   - List Categories:
      - Endpoint: GET /api/categories/
      - Description: Retrieve a list of all available categories.
    
   - List Tags:
      - Endpoint: GET /api/tags/
      - Description: Retrieve a list of all available tags.

# Using PostgreSQL reasons-
1. The scalability and the feature set of the database it is really useful for projects that can be extended into bigger projects
2. The data integrity of the database helps with the consistency and reliability of the data
3. It is open source and community friendly

# Outputs of the code
## API endpoints tested on postman
### Adding items to the dashboard
![0F20EF3F-3AC7-464F-B2DC-E51DF42CBA06](https://github.com/AarsheeB/kaizntree/assets/48876044/301dc468-6c80-4e91-ab38-dd24587d582c)
![1D283BF8-29D7-4B20-8371-0E76B735A40E](https://github.com/AarsheeB/kaizntree/assets/48876044/53108e60-b0e1-4ae4-af35-6d00295175f5)
### Creating a token to authenticate it
![23C49D51-4FC3-4D3E-B1CE-587C563E72D8](https://github.com/AarsheeB/kaizntree/assets/48876044/821a0f86-4346-41b2-93e8-7bb846aa50f5)
### Admin page
![358281B9-1188-46E3-8DE2-177E87122175](https://github.com/AarsheeB/kaizntree/assets/48876044/74144336-2f2e-426c-8d5a-9cfab194e18b)

![3B797ADA-249C-4F3A-9187-F579BCB96A70](https://github.com/AarsheeB/kaizntree/assets/48876044/7796bb12-72f1-4e79-a1fb-d65ae533ad8f)
![6D0579D8-9647-416A-AFE7-2E0B050BD0FE](https://github.com/AarsheeB/kaizntree/assets/48876044/b5be0229-3bab-4c9b-b8f4-78851411c556)
### Login Page using HTML
![9AC09A6F-2449-4D6C-AB22-CC61F8092FF9](https://github.com/AarsheeB/kaizntree/assets/48876044/8c235fcb-d12e-4455-9936-b591fa28a1e8)
### Displaying all the items on the dashboard
![C9091F8C-EDF6-47BD-9DE5-E1A5C08EF2DA](https://github.com/AarsheeB/kaizntree/assets/48876044/289ddc22-194f-421b-8f31-7f86047b41bd)
### Login page using React
![FE5A81D6-7545-4799-83D3-E019B9CE3222](https://github.com/AarsheeB/kaizntree/assets/48876044/d67bc00e-5ee1-49c8-8fcd-72f2fcbade31)

### API endpoints
 http://127.0.0.1:8000/













 

