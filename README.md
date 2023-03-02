# Book Store Project

## steps to follow to build and run the project

1) Run the migrations command to create migration file for project models
`python manage.py makemigrations`

2) Run migrate command to migrate all the created migration to DB `python manage.py migrate`

3) Run runserver `python manage.py runserver`

####Note: before testing any apis, please create user using `python manage.py createsuperuser`
For Output visit this url `http://127.0.0.1:8000/`

##APIs are:

* For login `http://127.0.0.1:8000/users/login`
* For logout `http://127.0.0.1:8000/users/logout`
* For books data `http://127.0.0.1:8000/books/get_book?q=`
