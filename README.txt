INSTRUCTIONS (assuming Python, django, and djangorestframework already installed in your machine)

1. Download the project folder from github repository.

2. Press Windows + R key and type cmd to open the Command Prompt terminal.

3. Change the directory to the project folder directory.

4. Run cd venv/Scripts

5. Run activate

6. Run cd.. (x2) to get back to the project folder directory

7. Run python manage.py runserver

8. Go to the localhost in your browser (http://localhost:8000/)

9. This project didn't have home views but there are 3 main views for this project.
	a) List View: http://localhost:8000/inventory/
	b) API Endpoint: http://localhost:8000/api/inventory/
	c) Admin Panel: http://localhost:8000/admin/

10. List View and API Endpoint are straightforward to use.

11. For the Admin Panel, use the following credentials
	Username : irsyad
	Password : irsyadsanuri

12. In the inventory tabs, admin has the permission to create, read, update, and delete items (CRUD) for Inventorys and Suppliers

13. To do the testing, close the server by pressing Ctrl + shift + C in the Command Prompt terminal and Run python manage.py test.
