INSTRUCTIONS (assuming Python, django, and djangorestframework already installed in your machine)

1. Download the "Django Inventory Assignment - Kiratech" project folder from github repository.

2. Press Windows + R key to and type cmd to open Command Promt terminal.

3. Change the directory to project folder directory.

4. Run cd venv/Scripts

5. Run activate

6. Run cd.. (x2) to get to back to project folder directory

7. Run python manage.py runserver

8. Go to the localhost in your browser (http://localhost:8000/)

9. This project didn't have home views but there's 3 main views for this project.
	a) List View: http://localhost:8000/inventory/
	b) API Endpoint: http://localhost:8000/api/inventory/
	c) Admin Panel: http://localhost:8000/admin/

10. List View and API Endpoint are straight forward to use.

11. For Admin Panel, use the following credentials
	Username : irsyad
	Password : irsyadsanuri

12. In the inventory tabs, admin has the permission to create, read, update, and delete items (CRUD) for Inventorys and Suppliers

13. To do the testing, close the server by pressing Ctrl + shift + C and Run python manage.py test.